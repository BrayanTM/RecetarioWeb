from rest_framework.views import APIView
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from http import HTTPStatus
from datetime import datetime
import os
from .models import Recipe
from .serializers import RecipeSerializer
from security.decorators import logging_decorator
from jose import JWTError, jwt


# Create your views here.
class RecipeListView(APIView):
    
    def get(self, request):
        recipes = Recipe.objects.order_by('-id').all()
        serializer = RecipeSerializer(recipes, many=True)
        return JsonResponse({'recipes': serializer.data}, status=HTTPStatus.OK)


    @logging_decorator()
    def post(self, request):
        # Validar el archivo antes de procesarlo
        uploaded_file = request.FILES.get('file')
        
        if not uploaded_file:
            return JsonResponse({'error': 'No file provided.'}, status=HTTPStatus.BAD_REQUEST)
        
        if uploaded_file.content_type not in ['image/jpeg', 'image/png'] or uploaded_file.size <= 0:
            return JsonResponse({'error': 'Invalid file type. Only JPEG and PNG are allowed.'}, status=HTTPStatus.BAD_REQUEST)

        # Generar nombre único para el archivo (pero NO guardarlo todavía)
        timestamp = datetime.now().timestamp()
        extension = os.path.splitext(uploaded_file.name)[1]
        filename = f"{int(timestamp)}{extension}"

        # Obtener el usuario del token JWT
        auth_header = request.headers.get('Authorization').split(' ')
        try:
            decoded_token = jwt.decode(auth_header[1], os.getenv("SECRET_KEY"), algorithms=[os.getenv("JWT_ALGORITHM")])
            user_id = decoded_token.get('user_id')
        except JWTError as e:
            return JsonResponse({'error': 'Invalid token.'}, status=HTTPStatus.UNAUTHORIZED)

        # Validar los datos del request (sin picture ni user)
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            # Solo si la validación es exitosa, guardar la imagen
            fs = FileSystemStorage()
            fs.save(f"recipes/{filename}", uploaded_file)
            
            # Guardar la receta con los campos controlados por el servidor
            user = User.objects.get(pk=user_id)
            recipe = serializer.save(user=user, picture=filename)
            return JsonResponse({'recipe': RecipeSerializer(recipe).data}, status=HTTPStatus.CREATED)
        
        # Si la validación falla, NO se guarda la imagen
        return JsonResponse({'errors': serializer.errors}, status=HTTPStatus.BAD_REQUEST)


class RecipeDetailView(APIView):
    def get(self, request, pk):
        try:
            recipe = Recipe.objects.get(pk=pk)
            serializer = RecipeSerializer(recipe)
            return JsonResponse({'recipe': serializer.data}, status=HTTPStatus.OK)
        except Recipe.DoesNotExist:
            return JsonResponse({'error': 'Recipe not found'}, status=HTTPStatus.NOT_FOUND)


    @logging_decorator()
    def put(self, request, pk):
        try:
            recipe = Recipe.objects.get(pk=pk)
            
            # Manejar la subida de archivo si existe
            uploaded_file = request.FILES.get('file')
            filename = None
            old_picture = recipe.picture  # Guardar referencia a la imagen antigua
            
            if uploaded_file:
                # Verificar que el archivo sea válido y tenga contenido
                if uploaded_file.content_type not in ['image/jpeg', 'image/png'] or uploaded_file.size <= 0:
                    return JsonResponse({'error': 'Invalid file type. Only JPEG and PNG are allowed.'}, status=HTTPStatus.BAD_REQUEST)
                
                # Generar nombre único para el archivo (pero NO guardarlo todavía)
                timestamp = datetime.now().timestamp()
                extension = os.path.splitext(uploaded_file.name)[1]
                filename = f"{int(timestamp)}{extension}"
            
            # Validar los datos del request (sin picture)
            serializer = RecipeSerializer(recipe, data=request.data, partial=True)
            if serializer.is_valid():
                # Solo si la validación es exitosa, procesar la imagen
                if filename:
                    # Eliminar archivo anterior si existe
                    if old_picture:
                        old_file_path = f"uploads/recipes/{old_picture}"
                        if os.path.exists(old_file_path):
                            os.remove(old_file_path)
                    
                    # Guardar el nuevo archivo
                    fs = FileSystemStorage()
                    fs.save(f"recipes/{filename}", uploaded_file)
                    
                    # Guardar con el nuevo nombre de archivo
                    serializer.save(picture=filename)
                else:
                    # Guardar sin modificar la imagen
                    serializer.save()
                
                return JsonResponse({'recipe': serializer.data}, status=HTTPStatus.OK)
            
            # Si la validación falla, NO se modifica la imagen
            return JsonResponse({'errors': serializer.errors}, status=HTTPStatus.BAD_REQUEST)
        except Recipe.DoesNotExist:
            return JsonResponse({'error': 'Recipe not found'}, status=HTTPStatus.NOT_FOUND)


    @logging_decorator()
    def delete(self, request, pk):
        try:
            recipe = Recipe.objects.get(pk=pk)
            
            # Eliminar archivo físico si existe
            if recipe.picture:
                file_path = f"uploads/recipes/{recipe.picture}"
                if os.path.exists(file_path):
                    os.remove(file_path)
            
            recipe.delete()
            return JsonResponse({'message': 'Recipe deleted successfully'}, status=HTTPStatus.OK)
        except Recipe.DoesNotExist:
            return JsonResponse({'error': 'Recipe not found'}, status=HTTPStatus.NOT_FOUND)