from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse, Http404
# Upload
from django.core.files.storage import FileSystemStorage
import os
from datetime import datetime
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


# Create your views here.
class ClassExample(APIView):
    
    @swagger_auto_schema(
        operation_description="Example GET endpoint with query parameters",
        manual_parameters=[
            openapi.Parameter('id', openapi.IN_QUERY, description="Optional ID parameter", type=openapi.TYPE_STRING),
            openapi.Parameter('slug', openapi.IN_QUERY, description="Optional slug parameter", type=openapi.TYPE_STRING),
        ],
        responses={
            200: openapi.Response(
                description="Success",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'message': openapi.Schema(type=openapi.TYPE_STRING),
                        'id': openapi.Schema(type=openapi.TYPE_STRING),
                        'slug': openapi.Schema(type=openapi.TYPE_STRING)
                    }
                )
            )
        }
    )
    def get(self, request):
        return JsonResponse({"message": "Hello, this is a class-based view example!", "id": request.GET.get('id', 'No ID provided'), "slug": request.GET.get('slug', 'No Slug provided')}, status=200)
    

    @swagger_auto_schema(
        operation_description="Example POST endpoint",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['email', 'password'],
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email address'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
            }
        ),
        responses={
            201: openapi.Response(
                description="Success",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'message': openapi.Schema(type=openapi.TYPE_STRING)
                    }
                )
            ),
            404: 'Email and Password are required fields'
        }
    )
    def post(self, request):
        if request.data.get('email') is None or request.data.get('password') is None:
            raise Http404("Email and Password are required fields.")
        
        return JsonResponse({"message": f"POST request received! | Email: {request.data.get('email', 'No Email provided')} | Password: {request.data.get('password', 'No Password provided')}"}, status=201)


class ClassExampleParams(APIView):

    @swagger_auto_schema(
        operation_description="Example GET endpoint with URL parameter",
        responses={
            200: openapi.Response(
                description="Success",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'message': openapi.Schema(type=openapi.TYPE_STRING),
                        'id': openapi.Schema(type=openapi.TYPE_INTEGER)
                    }
                )
            )
        }
    )
    def get(self, request, id):
        return JsonResponse({"message": "Hello, this is a class-based view example with ID:", "id": id})


    @swagger_auto_schema(
        operation_description="Example PUT endpoint with URL parameter",
        responses={
            200: openapi.Response(
                description="Success",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'message': openapi.Schema(type=openapi.TYPE_STRING),
                        'id': openapi.Schema(type=openapi.TYPE_INTEGER)
                    }
                )
            )
        }
    )
    def put(self, request, id):
        return JsonResponse({"message": "PUT request received for ID:", "id": id})


    @swagger_auto_schema(
        operation_description="Example DELETE endpoint with URL parameter",
        responses={
            200: openapi.Response(
                description="Success",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'message': openapi.Schema(type=openapi.TYPE_STRING),
                        'id': openapi.Schema(type=openapi.TYPE_INTEGER)
                    }
                )
            )
        }
    )
    def delete(self, request, id):
        return JsonResponse({"message": "DELETE request received for ID:", "id": id})


class FileUploadExample(APIView):

    @swagger_auto_schema(
        operation_description="Example file upload endpoint. Use multipart/form-data.",
        manual_parameters=[
            openapi.Parameter(
                'file',
                openapi.IN_FORM,
                description="File to upload",
                type=openapi.TYPE_FILE,
                required=True
            ),
        ],
        consumes=['multipart/form-data'],
        responses={
            201: openapi.Response(
                description="File uploaded successfully",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'message': openapi.Schema(type=openapi.TYPE_STRING)
                    }
                )
            )
        }
    )
    def post(self, request):
        file_system = FileSystemStorage()
        date = datetime.now()
        # Save the uploaded file with a timestamp prefix to avoid name collisions
        name_file = f"{datetime.timestamp(date)}{os.path.splitext(str(request.FILES['file']))[1]}"
        file_system.save(f"example/{name_file}", request.FILES['file'])
        file_system.url(request.FILES['file'])
        return JsonResponse({"message": "File uploaded successfully!"}, status=201)