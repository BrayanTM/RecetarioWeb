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
        # Security improvement: URL points to frontend, not backend API
        url = f'{os.getenv("BASE_URL_FRONTEND")}/verify-email?token={token}'

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
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <style>
                    body {{
                        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                        line-height: 1.6;
                        color: #333;
                        max-width: 600px;
                        margin: 0 auto;
                        padding: 0;
                        background-color: #f4f4f4;
                    }}
                    .container {{
                        background-color: #ffffff;
                        margin: 20px auto;
                        border-radius: 12px;
                        overflow: hidden;
                        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                    }}
                    .header {{
                        background: linear-gradient(135deg, #FF6B6B 0%, #FF8E53 100%);
                        color: white;
                        padding: 40px 30px;
                        text-align: center;
                    }}
                    .header h1 {{
                        margin: 0;
                        font-size: 28px;
                        font-weight: 600;
                    }}
                    .header p {{
                        margin: 10px 0 0 0;
                        font-size: 16px;
                        opacity: 0.95;
                    }}
                    .content {{
                        padding: 40px 30px;
                    }}
                    .greeting {{
                        font-size: 18px;
                        color: #333;
                        margin-bottom: 20px;
                    }}
                    .greeting strong {{
                        color: #FF6B6B;
                    }}
                    .message {{
                        font-size: 15px;
                        color: #555;
                        line-height: 1.8;
                        margin-bottom: 30px;
                    }}
                    .button-container {{
                        text-align: center;
                        margin: 35px 0;
                    }}
                    .verify-button {{
                        display: inline-block;
                        padding: 16px 40px;
                        background: linear-gradient(135deg, #FF6B6B 0%, #FF8E53 100%);
                        color: white !important;
                        text-decoration: none;
                        border-radius: 50px;
                        font-weight: 600;
                        font-size: 16px;
                        box-shadow: 0 4px 15px rgba(255, 107, 107, 0.3);
                        transition: transform 0.3s ease;
                    }}
                    .verify-button:hover {{
                        transform: translateY(-2px);
                        box-shadow: 0 6px 20px rgba(255, 107, 107, 0.4);
                    }}
                    .info-box {{
                        background: #f8f9fa;
                        border-left: 4px solid #FF6B6B;
                        padding: 20px;
                        margin: 25px 0;
                        border-radius: 4px;
                    }}
                    .info-box p {{
                        margin: 0;
                        font-size: 14px;
                        color: #666;
                    }}
                    .alternative-link {{
                        margin-top: 25px;
                        padding: 20px;
                        background: #f8f9fa;
                        border-radius: 8px;
                        word-break: break-all;
                    }}
                    .alternative-link p {{
                        margin: 0 0 10px 0;
                        font-size: 13px;
                        color: #666;
                    }}
                    .alternative-link a {{
                        color: #FF6B6B;
                        text-decoration: none;
                        font-size: 12px;
                    }}
                    .footer {{
                        background: #2c3e50;
                        color: #ecf0f1;
                        padding: 30px;
                        text-align: center;
                    }}
                    .footer p {{
                        margin: 8px 0;
                        font-size: 13px;
                        line-height: 1.6;
                    }}
                    .footer strong {{
                        color: #FF8E53;
                    }}
                    .divider {{
                        height: 1px;
                        background: linear-gradient(to right, transparent, #ddd, transparent);
                        margin: 30px 0;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <h1>🍳 Welcome to Cookbook</h1>
                        <p>Your personalized digital recipe book</p>
                    </div>
                    <div class="content">
                        <div class="greeting">
                            Hello <strong>{request.data['first_name']}</strong>! 👋
                        </div>
                        <div class="message">
                            We're thrilled to have you with us. You've taken the first step to discover,
                            create, and share amazing recipes.
                        </div>
                        <div class="message">
                            To start your culinary adventure, we need to verify your email address.
                            It will only take a second:
                        </div>
                        <div class="button-container">
                            <a href="{url}" class="verify-button">✓ Verify My Account</a>
                        </div>
                        <div class="info-box">
                            <p>
                                <strong>⏱️ Important:</strong> This verification link is unique and secure.
                                We recommend completing the verification as soon as possible.
                            </p>
                        </div>
                        <div class="divider"></div>
                        <div class="alternative-link">
                            <p><strong>Button not working?</strong> Copy and paste this link into your browser:</p>
                            <a href="{url}">{url}</a>
                        </div>
                        <div class="divider"></div>
                        <div class="message" style="font-size: 13px; color: #999; margin-top: 20px;">
                            <strong>🔒 Security:</strong> If you didn't create this account, you can safely ignore this email.
                            Your email address will not be registered in our system without verification.
                        </div>
                    </div>
                    <div class="footer">
                        <p><strong>Cookbook</strong> - Your digital recipe book</p>
                        <p>This is an automated email, please do not reply to this message.</p>
                        <p style="margin-top: 15px; opacity: 0.8;">
                            © 2025 Cookbook. All rights reserved.
                        </p>
                    </div>
                </div>
            </body>
            </html>
            """
            utilities.send_email(mail, "✓ Verify Your Cookbook Account", request.data['email'])

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=HTTPStatus.BAD_REQUEST)

        return JsonResponse({"message": "User registered successfully. Please verify your email.", "verification_url": url}, status=HTTPStatus.CREATED)


class SecurityVerifyView(APIView):
    @swagger_auto_schema(
        operation_description="Verify user email with the provided token.",
        manual_parameters=[
            openapi.Parameter(
                'uid',
                openapi.IN_QUERY,
                description="Verification token sent to user's email",
                type=openapi.TYPE_STRING,
                required=True
            )
        ],
        responses={
            200: openapi.Response(
                description="Email verified successfully",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'success': openapi.Schema(type=openapi.TYPE_BOOLEAN),
                        'message': openapi.Schema(type=openapi.TYPE_STRING),
                        'user': openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'id': openapi.Schema(type=openapi.TYPE_STRING),
                                'username': openapi.Schema(type=openapi.TYPE_STRING),
                                'email': openapi.Schema(type=openapi.TYPE_STRING),
                            }
                        )
                    }
                )
            ),
            400: 'Bad Request - Invalid token or user not found'
        }
    )
    def get(self, request):
        token = request.query_params.get('uid')

        if token == None or not str(token).strip():
            return JsonResponse({
                "success": False,
                "error": "Token is required"
            }, status=HTTPStatus.BAD_REQUEST)

        try:
            user_metadata = UsersMetadata.objects.filter(token=token).filter(user__is_active=False).get()
            user = User.objects.get(id=user_metadata.user_id)
            user.is_active = True
            user.save()
            user_metadata.token = ""
            user_metadata.save()

            return JsonResponse({
                "success": True,
                "message": "Email verified successfully! You can now log in to your account.",
                "user": {
                    "id": str(user.id),
                    "username": user.username,
                    "email": user.email
                }
            }, status=HTTPStatus.OK)

        except UsersMetadata.DoesNotExist:
            return JsonResponse({
                "success": False,
                "error": "Invalid or expired verification token. Please request a new verification email."
            }, status=HTTPStatus.BAD_REQUEST)
        except User.DoesNotExist:
            return JsonResponse({
                "success": False,
                "error": "User not found"
            }, status=HTTPStatus.BAD_REQUEST)


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
