from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponseRedirect
from http import HTTPStatus
from .models import UsersMetadata
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from utilities import utilities
from datetime import datetime, timedelta
from jose import JWTError, jwt
import uuid
import os
import time
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

#from .serializers import


# Create your views here.
class SecurityRegisterView(APIView):
    @swagger_auto_schema(
        operation_description="Register a new user. Sends a verification email.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['username', 'password', 'email', 'first_name', 'last_name'],
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email address'),
                'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='First name'),
                'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='Last name'),
            }
        ),
        responses={
            201: openapi.Response(
                description="User registered successfully",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'message': openapi.Schema(type=openapi.TYPE_STRING),
                        'verification_url': openapi.Schema(type=openapi.TYPE_STRING)
                    }
                )
            ),
            400: 'Bad Request - Invalid data or email already in use'
        }
    )
    def post(self, request):
        # Implement registration logic here
        if request.data.get('username') == None or not request.data.get('username').strip():
            return JsonResponse({"error": "Username and password are required"}, status=HTTPStatus.BAD_REQUEST)
        if request.data.get('password') == None or not request.data.get('password').strip():
            return JsonResponse({"error": "Username and password are required"}, status=HTTPStatus.BAD_REQUEST)
        if request.data.get('email') == None or not request.data.get('email').strip():
            return JsonResponse({"error": "Email is required"}, status=HTTPStatus.BAD_REQUEST)
        if User.objects.filter(email=request.data['email']).exists():
            return JsonResponse({"error": "Email already in use"}, status=HTTPStatus.BAD_REQUEST)

        token = uuid.uuid4()
        url = f'{os.getenv("BASE_URL")}api/v1/security/verify/{token}'

        try:
            user = User.objects.create_user(
                username=request.data['username'],
                password=request.data['password'],
                email=request.data['email'],
                first_name=request.data['first_name'],
                last_name=request.data['last_name'],
                is_active=False
            )
            UsersMetadata.objects.create(user_id=user.id, token=token)

            mail = f"""
            <h1>Welcome to RecetarioWeb {request.data['first_name']}</h1>
            <p>Thank you for registering. Please verify your email by clicking the link below:</p>
            <a href="{url}">Verify Email</a>
            <p>If you did not register, please ignore this email.</p>
            """
            utilities.send_email(mail, "Verify your email", request.data['email'])

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=HTTPStatus.BAD_REQUEST)

        return JsonResponse({"message": "User registered successfully. Please verify your email.", "verification_url": url}, status=HTTPStatus.CREATED)


class SecurityVerifyView(APIView):
    @swagger_auto_schema(
        operation_description="Verify user email with the provided token. Redirects to frontend on success.",
        responses={
            302: 'Redirect to frontend',
            400: 'Bad Request - Invalid token or user not found'
        }
    )
    def get(self, request, token):
        if token == None or not str(token).strip():
            return JsonResponse({"error": "Token is required"}, status=HTTPStatus.BAD_REQUEST)
        try:
            user_metadata = UsersMetadata.objects.filter(token=token).filter(user__is_active=False).get()
            user = User.objects.get(id=user_metadata.user_id)
            user.is_active = True
            user.save()
            user_metadata.token = ""
            user_metadata.save()
            return HttpResponseRedirect(os.getenv("BASE_URL_FRONTEND"))
        except UsersMetadata.DoesNotExist:
            return JsonResponse({"error": "Invalid token"}, status=HTTPStatus.BAD_REQUEST)
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=HTTPStatus.BAD_REQUEST)


class SecurityLoginView(APIView):
    @swagger_auto_schema(
        operation_description="Login with email and password. Returns JWT token on success.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['email', 'password'],
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email address'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
            }
        ),
        responses={
            200: openapi.Response(
                description="Login successful",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'user_id': openapi.Schema(type=openapi.TYPE_STRING),
                        'name': openapi.Schema(type=openapi.TYPE_STRING),
                        'token': openapi.Schema(type=openapi.TYPE_STRING, description='JWT token')
                    }
                )
            ),
            401: 'Unauthorized - Invalid credentials or account not active',
            500: 'Internal Server Error - Token generation failed'
        }
    )
    def post(self, request):
        # Implement login logic here
        if request.data.get('email') == None or not request.data.get('email').strip():
            return JsonResponse({"error": "Email and password are required"}, status=HTTPStatus.BAD_REQUEST)
        if request.data.get('password') == None or not request.data.get('password').strip():
            return JsonResponse({"error": "Email and password are required"}, status=HTTPStatus.BAD_REQUEST)

        try:
            user = User.objects.filter(email=request.data['email']).get()
        except User.DoesNotExist:
            return JsonResponse({"error": "Invalid credentials"}, status=HTTPStatus.UNAUTHORIZED)

        if not user.is_active:
            return JsonResponse({"error": "Account is not active. Please verify your email."}, status=HTTPStatus.UNAUTHORIZED)

        authenticated = authenticate(request, username=user.username, password=request.data['password'])
        if authenticated is not None:
            date_now = datetime.now()
            after = date_now + timedelta(days=1)
            date = int(datetime.timestamp(after))
            payload = {
                "user_id": str(user.id),
                "iss": os.getenv("BASE_URL"),
                "iat": int(time.time()),
                "exp": date
            }
            try:
                token = jwt.encode(payload, os.getenv("SECRET_KEY"), algorithm=os.getenv("JWT_ALGORITHM"))
                return JsonResponse({"user_id": str(user.id), "name": user.username, "token": token}, status=HTTPStatus.OK)
            except JWTError as e:
                return JsonResponse({"error": "Token generation failed"}, status=HTTPStatus.INTERNAL_SERVER_ERROR)
        else:
            return JsonResponse({"error": "Invalid credentials"}, status=HTTPStatus.UNAUTHORIZED)
