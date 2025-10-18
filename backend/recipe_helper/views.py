from security.decorators import logging_decorator
from recipes.serializers import RecipeSerializer
from recipes.models import Recipe
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.http import JsonResponse
from http import HTTPStatus

# Create your views here.
class RecipeUserPanel(APIView):
    
    
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
    
    
    def get(self, request, slug):
        # Validar que la receta exista
        try:
            recipe = Recipe.objects.get(slug=slug)
        except Recipe.DoesNotExist:
            return JsonResponse({'error': 'Recipe not found.'}, status=HTTPStatus.NOT_FOUND)
        
        serializer = RecipeSerializer(recipe)
        return JsonResponse({'recipe': serializer.data}, status=HTTPStatus.OK)


class RecipeListView(APIView):
    
    def get(self, request):
        recipes = Recipe.objects.order_by('?').all()[:3]
        serializer = RecipeSerializer(recipes, many=True)
        return JsonResponse({'recipes': serializer.data}, status=HTTPStatus.OK)


class RecipeListSearch(APIView):
    
    
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