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
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


# Create your views here.
class RecipeListView(APIView):
    
    @swagger_auto_schema(
        operation_description="Get all recipes ordered by ID (descending)",
        responses={
            200: openapi.Response(
                description="List of recipes",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'recipes': openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(type=openapi.TYPE_OBJECT)
                        )
                    }
                )
            )
        }
    )
    def get(self, request):
        recipes = Recipe.objects.order_by('-id').all()
        serializer = RecipeSerializer(recipes, many=True)
        return JsonResponse({'recipes': serializer.data}, status=HTTPStatus.OK)


    @swagger_auto_schema(
        operation_description="Create a new recipe with image upload. Requires authentication. Use multipart/form-data.",
        manual_parameters=[
            openapi.Parameter(
                'Authorization',
                openapi.IN_HEADER,
                description="JWT token (Bearer <token>)",
                type=openapi.TYPE_STRING,
                required=True
            ),
            openapi.Parameter(
                'file',
                openapi.IN_FORM,
                description="Recipe image (JPEG or PNG)",
                type=openapi.TYPE_FILE,
                required=True
            ),
            openapi.Parameter(
                'name',
                openapi.IN_FORM,
                description="Recipe name",
                type=openapi.TYPE_STRING,
                required=True
            ),
            openapi.Parameter(
                'time',
                openapi.IN_FORM,
                description="Cooking time",
                type=openapi.TYPE_STRING,
                required=True
            ),
            openapi.Parameter(
                'description',
                openapi.IN_FORM,
                description="Recipe description",
                type=openapi.TYPE_STRING,
                required=True
            ),
            openapi.Parameter(
                'category',
                openapi.IN_FORM,
                description="Category ID",
                type=openapi.TYPE_INTEGER,
                required=True
            ),
        ],
        consumes=['multipart/form-data'],
        responses={
            201: openapi.Response(
                description="Recipe created successfully",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'recipe': openapi.Schema(type=openapi.TYPE_OBJECT)
                    }
                )
            ),
            400: 'Bad Request - Invalid file or data',
            401: 'Unauthorized - Invalid token',
        }
    )
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
    @swagger_auto_schema(
        operation_description="Get a specific recipe by ID",
        responses={
            200: openapi.Response(
                description="Recipe details",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'recipe': openapi.Schema(type=openapi.TYPE_OBJECT)
                    }
                )
            ),
            404: 'Recipe not found'
        }
    )
    def get(self, request, pk):
        try:
            recipe = Recipe.objects.get(pk=pk)
            serializer = RecipeSerializer(recipe)
            return JsonResponse({'recipe': serializer.data}, status=HTTPStatus.OK)
        except Recipe.DoesNotExist:
            return JsonResponse({'error': 'Recipe not found'}, status=HTTPStatus.NOT_FOUND)


    @swagger_auto_schema(
        operation_description="Update a recipe. Requires authentication. Can update image and/or recipe data. Use multipart/form-data. All fields are optional.",
        manual_parameters=[
            openapi.Parameter(
                'Authorization',
                openapi.IN_HEADER,
                description="JWT token (Bearer <token>)",
                type=openapi.TYPE_STRING,
                required=True
            ),
            openapi.Parameter(
                'file',
                openapi.IN_FORM,
                description="New recipe image (JPEG or PNG) - optional",
                type=openapi.TYPE_FILE,
                required=False
            ),
            openapi.Parameter(
                'name',
                openapi.IN_FORM,
                description="Recipe name - optional",
                type=openapi.TYPE_STRING,
                required=False
            ),
            openapi.Parameter(
                'time',
                openapi.IN_FORM,
                description="Cooking time - optional",
                type=openapi.TYPE_STRING,
                required=False
            ),
            openapi.Parameter(
                'description',
                openapi.IN_FORM,
                description="Recipe description - optional",
                type=openapi.TYPE_STRING,
                required=False
            ),
            openapi.Parameter(
                'category',
                openapi.IN_FORM,
                description="Category ID - optional",
                type=openapi.TYPE_INTEGER,
                required=False
            ),
        ],
        consumes=['multipart/form-data'],
        responses={
            200: openapi.Response(
                description="Recipe updated successfully",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'recipe': openapi.Schema(type=openapi.TYPE_OBJECT)
                    }
                )
            ),
            400: 'Bad Request - Invalid file or data',
            404: 'Recipe not found'
        }
    )
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


    @swagger_auto_schema(
        operation_description="Delete a recipe and its associated image. Requires authentication.",
        manual_parameters=[
            openapi.Parameter(
                'Authorization',
                openapi.IN_HEADER,
                description="JWT token (Bearer <token>)",
                type=openapi.TYPE_STRING,
                required=True
            ),
        ],
        responses={
            200: openapi.Response(
                description="Recipe deleted successfully",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'message': openapi.Schema(type=openapi.TYPE_STRING)
                    }
                )
            ),
            404: 'Recipe not found'
        }
    )
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