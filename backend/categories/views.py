from rest_framework.views import APIView
from django.http import JsonResponse, Http404
from http import HTTPStatus
from django.utils.text import slugify
from .models import Category
from .serializers import CategorySerializer


# Create your views here.
class CategoryList(APIView):
    def get(self, request):
        data = Category.objects.order_by('-id').all()
        serializer = CategorySerializer(data, many=True)
        return JsonResponse({'categories': serializer.data}, status=HTTPStatus.OK)
    

    def post(self, request):
        if request.data.get('name') is None or not request.data.get('name').strip():
            return JsonResponse({'error': 'Name is required'}, status=HTTPStatus.BAD_REQUEST)
        try:
            Category.objects.create(name=request.data.get('name'))
            return JsonResponse({'message': 'Category created successfully'}, status=HTTPStatus.CREATED)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)


class CategoryDetail(APIView):
    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return JsonResponse({'category': serializer.data}, status=HTTPStatus.OK)
        except Category.DoesNotExist:
            raise Http404("Category not found")


    def put(self, request, pk):
        if request.data.get('name') is None or not request.data.get('name').strip():
            return JsonResponse({'error': 'Name is required'}, status=HTTPStatus.BAD_REQUEST)
        try:
            category = Category.objects.get(pk=pk)
            category.name = request.data.get('name')
            category.slug = slugify(request.data.get('name'))
            category.save()
            return JsonResponse({'message': 'Category updated successfully'}, status=HTTPStatus.OK)
        except Category.DoesNotExist:
            return JsonResponse({'error': 'Category not found'}, status=HTTPStatus.NOT_FOUND)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)


    def delete(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
            category.delete()
            return JsonResponse({'message': 'Category deleted successfully'}, status=HTTPStatus.OK)
        except Category.DoesNotExist:
            return JsonResponse({'error': 'Category not found'}, status=HTTPStatus.NOT_FOUND)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)

