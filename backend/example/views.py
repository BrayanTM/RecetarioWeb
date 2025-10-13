from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse, Http404
# Upload
from django.core.files.storage import FileSystemStorage
import os
from datetime import datetime


# Create your views here.
class ClassExample(APIView):
    

    def get(self, request):
        return JsonResponse({"message": "Hello, this is a class-based view example!", "id": request.GET.get('id', 'No ID provided'), "slug": request.GET.get('slug', 'No Slug provided')}, status=200)
    

    def post(self, request):
        if request.data.get('email') is None or request.data.get('password') is None:
            raise Http404("Email and Password are required fields.")
        
        return JsonResponse({"message": f"POST request received! | Email: {request.data.get('email', 'No Email provided')} | Password: {request.data.get('password', 'No Password provided')}"}, status=201)


class ClassExampleParams(APIView):


    def get(self, request, id):
        return JsonResponse({"message": "Hello, this is a class-based view example with ID:", "id": id})


    def put(self, request, id):
        return JsonResponse({"message": "PUT request received for ID:", "id": id})


    def delete(self, request, id):
        return JsonResponse({"message": "DELETE request received for ID:", "id": id})


class FileUploadExample(APIView):

    def post(self, request):
        file_system = FileSystemStorage()
        date = datetime.now()
        # Save the uploaded file with a timestamp prefix to avoid name collisions
        name_file = f"{datetime.timestamp(date)}{os.path.splitext(str(request.FILES['file']))[1]}"
        file_system.save(f"example/{name_file}", request.FILES['file'])
        file_system.url(request.FILES['file'])
        return JsonResponse({"message": "File uploaded successfully!"}, status=201)