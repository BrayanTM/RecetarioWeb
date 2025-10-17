from rest_framework.views import APIView
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from http import HTTPStatus
from datetime import datetime
import os
from .models import Recipe
from .serializers import RecipeSerializer
from security.decorators import logging_decorator


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
        
        # Agregar el nombre del archivo a request.data para validación
        request.data['picture'] = filename

        # Validar primero con el serializador
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            # Solo si la validación es exitosa, guardar la imagen
            fs = FileSystemStorage()
            fs.save(f"recipes/{filename}", uploaded_file)
            
            # Guardar la receta en la base de datos
            recipe = serializer.save()
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
                
                # Agregar el nombre del archivo a request.data para validación
                request.data['picture'] = filename
            
            # Validar primero con el serializador
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
                
                # Guardar los cambios en la base de datos
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