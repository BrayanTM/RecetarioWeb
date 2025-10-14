from rest_framework.views import APIView
from django.http import JsonResponse, Http404
from http import HTTPStatus
from .models import Category
from .serializers import CategorySerializer
from recipes.models import Recipe


# Create your views here.
class CategoryList(APIView):
    def get(self, request):
        categories = Category.objects.order_by('-id').all()
        serializer = CategorySerializer(categories, many=True)
        return JsonResponse({'categories': serializer.data}, status=HTTPStatus.OK)
    

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            category = serializer.save()
            return JsonResponse({'category': CategorySerializer(category).data}, status=HTTPStatus.CREATED)
        return JsonResponse({'errors': serializer.errors}, status=HTTPStatus.BAD_REQUEST)


class CategoryDetail(APIView):
    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return JsonResponse({'category': serializer.data}, status=HTTPStatus.OK)
        except Category.DoesNotExist:
            raise Http404("Category not found")


    def put(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'category': serializer.data}, status=HTTPStatus.OK)
            return JsonResponse({'errors': serializer.errors}, status=HTTPStatus.BAD_REQUEST)
        except Category.DoesNotExist:
            return JsonResponse({'error': 'Category not found'}, status=HTTPStatus.NOT_FOUND)


    def delete(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return JsonResponse({'error': 'Category not found'}, status=HTTPStatus.NOT_FOUND)
        # No permitir eliminar si hay recetas asociadas
        if Recipe.objects.filter(category=category).exists():
            return JsonResponse({'error': 'Cannot delete category with associated recipes'}, status=HTTPStatus.BAD_REQUEST)

        category.delete()
        return JsonResponse({'message': 'Category deleted successfully'}, status=HTTPStatus.OK)