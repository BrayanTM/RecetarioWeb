from security.decorators import logging_decorator
from recipes.serializers import RecipeSerializer
from recipes.models import Recipe
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.http import JsonResponse
from http import HTTPStatus
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
class RecipeUserPanel(APIView):
    
    @swagger_auto_schema(
        operation_description="Get all recipes from a specific user. Requires authentication.",
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
                description="List of user recipes",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'recipes': openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(type=openapi.TYPE_OBJECT)
                        )
                    }
                )
            ),
            404: 'User not found'
        }
    )
    @logging_decorator()
    def get(self, request, pk):
        # Validar que el usuario exista
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found.'}, status=HTTPStatus.NOT_FOUND)
        
        # Obtener las recetas del usuario
        recipes = Recipe.objects.filter(user=user).order_by('-id').all()
        serializer = RecipeSerializer(recipes, many=True)
        return JsonResponse({'recipes': serializer.data}, status=HTTPStatus.OK)


class RecipeDetailView(APIView):
    
    @swagger_auto_schema(
        operation_description="Get a specific recipe by slug",
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
    def get(self, request, slug):
        # Validar que la receta exista
        try:
            recipe = Recipe.objects.get(slug=slug)
        except Recipe.DoesNotExist:
            return JsonResponse({'error': 'Recipe not found.'}, status=HTTPStatus.NOT_FOUND)
        
        serializer = RecipeSerializer(recipe)
        return JsonResponse({'recipe': serializer.data}, status=HTTPStatus.OK)


class RecipeListView(APIView):
    
    @swagger_auto_schema(
        operation_description="Get 3 random recipes",
        responses={
            200: openapi.Response(
                description="List of random recipes",
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
        recipes = Recipe.objects.order_by('?').all()[:3]
        serializer = RecipeSerializer(recipes, many=True)
        return JsonResponse({'recipes': serializer.data}, status=HTTPStatus.OK)


class RecipeListSearch(APIView):
    
    @swagger_auto_schema(
        operation_description="Search recipes by category and name",
        manual_parameters=[
            openapi.Parameter('category_id', openapi.IN_QUERY, description="Category ID (required)", type=openapi.TYPE_INTEGER, required=True),
            openapi.Parameter('search', openapi.IN_QUERY, description="Search term for recipe name (optional)", type=openapi.TYPE_STRING),
        ],
        responses={
            200: openapi.Response(
                description="List of filtered recipes",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'recipes': openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(type=openapi.TYPE_OBJECT)
                        )
                    }
                )
            ),
            400: 'Bad Request - category_id is required or invalid',
            404: 'Category not found'
        }
    )
    def get(self, request):
        if not request.GET.get('category_id') or request.GET.get('category_id') == None:
            return JsonResponse({'error': 'category_id and search parameters are required.'}, status=HTTPStatus.BAD_REQUEST)
        try:
            category_exists = Recipe.objects.filter(category_id=request.GET.get('category_id')).exists()
            if not category_exists:
                return JsonResponse({'error': 'Category not found.'}, status=HTTPStatus.NOT_FOUND)
        except ValueError:
            return JsonResponse({'error': 'Invalid category_id.'}, status=HTTPStatus.BAD_REQUEST)

        recipes = Recipe.objects.filter(category_id=request.GET.get('category_id'), name__icontains=request.GET.get('search')).order_by('-id').all()
        serializer = RecipeSerializer(recipes, many=True)
        return JsonResponse({'recipes': serializer.data}, status=HTTPStatus.OK)