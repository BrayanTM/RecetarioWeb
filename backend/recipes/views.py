from rest_framework.views import APIView
from django.http import JsonResponse, Http404
from django.core.files.storage import FileSystemStorage
from http import HTTPStatus
from datetime import datetime
import os
from .models import Recipe
from .serializers import RecipeSerializer


# Create your views here.
class RecipeListView(APIView):
    def get(self, request):
        recipes = Recipe.objects.order_by('-id').all()
        serializer = RecipeSerializer(recipes, many=True)
        return JsonResponse({'recipes': serializer.data}, status=HTTPStatus.OK)


    def post(self, request):
        # Manejar la subida de archivo si existe
        uploaded_file = request.FILES.get('file')
        filename = None
        
        if (uploaded_file.content_type=='image/jpeg' or uploaded_file.content_type=='image/png') and uploaded_file.size > 0:
            # Generar nombre único para el archivo
            timestamp = datetime.now().timestamp()
            extension = os.path.splitext(uploaded_file.name)[1]
            filename = f"{int(timestamp)}{extension}"
            
            # Guardar el archivo
            fs = FileSystemStorage()
            fs.save(f"recipes/{filename}", uploaded_file)
        else:
            return JsonResponse({'error': 'Invalid file type. Only JPEG and PNG are allowed.'}, status=HTTPStatus.BAD_REQUEST)

        # Agregar el nombre del archivo directamente a request.data
        if filename:
            request.data['picture'] = filename

        # Validar y guardar con el serializador
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            recipe = serializer.save()
            return JsonResponse({'recipe': RecipeSerializer(recipe).data}, status=HTTPStatus.CREATED)
        return JsonResponse({'errors': serializer.errors}, status=HTTPStatus.BAD_REQUEST)


class RecipeDetailView(APIView):
    def get(self, request, pk):
        try:
            recipe = Recipe.objects.get(pk=pk)
            serializer = RecipeSerializer(recipe)
            return JsonResponse({'recipe': serializer.data}, status=HTTPStatus.OK)
        except Recipe.DoesNotExist:
            return JsonResponse({'error': 'Recipe not found'}, status=HTTPStatus.NOT_FOUND)


    def put(self, request, pk):
        try:
            recipe = Recipe.objects.get(pk=pk)
            
            # Manejar la subida de archivo si existe
            uploaded_file = request.FILES.get('file')
            filename = None
            
            # Verificar que el archivo sea válido y tenga contenido
            if (uploaded_file.content_type=='image/jpeg' or uploaded_file.content_type=='image/png') and uploaded_file.size > 0:
                # Generar nombre único para el archivo
                timestamp = datetime.now().timestamp()
                extension = os.path.splitext(uploaded_file.name)[1]
                filename = f"{int(timestamp)}{extension}"
                
                # Eliminar archivo anterior si existe
                if recipe.picture:
                    old_file_path = f"uploads/recipes/{recipe.picture}"
                    if os.path.exists(old_file_path):
                        os.remove(old_file_path)
                
                # Guardar el archivo
                fs = FileSystemStorage()
                fs.save(f"recipes/{filename}", uploaded_file)
            else:
                if uploaded_file:
                    return JsonResponse({'error': 'Invalid file type. Only JPEG and PNG are allowed.'}, status=HTTPStatus.BAD_REQUEST)
            
            # Agregar el nombre del archivo directamente a request.data
            if filename:
                request.data['picture'] = filename
            
            serializer = RecipeSerializer(recipe, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'recipe': serializer.data}, status=HTTPStatus.OK)
            return JsonResponse({'errors': serializer.errors}, status=HTTPStatus.BAD_REQUEST)
        except Recipe.DoesNotExist:
            return JsonResponse({'error': 'Recipe not found'}, status=HTTPStatus.NOT_FOUND)


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