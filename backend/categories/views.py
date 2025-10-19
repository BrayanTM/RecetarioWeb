from rest_framework.views import APIView
from django.http import JsonResponse, Http404
from http import HTTPStatus
from .models import Category
from .serializers import CategorySerializer
from recipes.models import Recipe
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


# Create your views here.
class CategoryList(APIView):
    @swagger_auto_schema(
        operation_description="Get all categories ordered by ID (descending)",
        responses={
            200: openapi.Response(
                description="List of categories",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'categories': openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(type=openapi.TYPE_OBJECT)
                        )
                    }
                )
            )
        }
    )
    def get(self, request):
        categories = Category.objects.order_by('-id').all()
        serializer = CategorySerializer(categories, many=True)
        return JsonResponse({'categories': serializer.data}, status=HTTPStatus.OK)
    

    @swagger_auto_schema(
        operation_description="Create a new category",
        request_body=CategorySerializer,
        responses={
            201: openapi.Response(
                description="Category created successfully",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'category': openapi.Schema(type=openapi.TYPE_OBJECT)
                    }
                )
            ),
            400: 'Bad Request - Invalid data'
        }
    )
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            category = serializer.save()
            return JsonResponse({'category': CategorySerializer(category).data}, status=HTTPStatus.CREATED)
        return JsonResponse({'errors': serializer.errors}, status=HTTPStatus.BAD_REQUEST)


class CategoryDetail(APIView):
    @swagger_auto_schema(
        operation_description="Get a specific category by ID",
        responses={
            200: openapi.Response(
                description="Category details",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'category': openapi.Schema(type=openapi.TYPE_OBJECT)
                    }
                )
            ),
            404: 'Category not found'
        }
    )
    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return JsonResponse({'category': serializer.data}, status=HTTPStatus.OK)
        except Category.DoesNotExist:
            raise Http404("Category not found")


    @swagger_auto_schema(
        operation_description="Update a category (partial update supported)",
        request_body=CategorySerializer,
        responses={
            200: openapi.Response(
                description="Category updated successfully",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'category': openapi.Schema(type=openapi.TYPE_OBJECT)
                    }
                )
            ),
            400: 'Bad Request - Invalid data',
            404: 'Category not found'
        }
    )
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


    @swagger_auto_schema(
        operation_description="Delete a category. Cannot delete if there are associated recipes.",
        responses={
            200: openapi.Response(
                description="Category deleted successfully",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'message': openapi.Schema(type=openapi.TYPE_STRING)
                    }
                )
            ),
            400: 'Bad Request - Cannot delete category with associated recipes',
            404: 'Category not found'
        }
    )
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