from rest_framework.views import APIView
from django.http import JsonResponse
from http import HTTPStatus
from .serializers import ContactMessageSerializer
from utilities import utilities
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
import os


# Create your views here.
class ContactView(APIView):

    @swagger_auto_schema(
        operation_description="Submit a contact message",
        request_body=ContactMessageSerializer,
        responses={
            201: ContactMessageSerializer,
            400: 'Bad Request',
        },
    )
    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # Send email notification
            try:
                body = f"""
                <!DOCTYPE html>
                <html lang="es">
                <head>
                    <meta charset="UTF-8">
                    <style>
                        body {{
                            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                            line-height: 1.6;
                            color: #333;
                            max-width: 600px;
                            margin: 0 auto;
                            padding: 20px;
                        }}
                        .header {{
                            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                            color: white;
                            padding: 30px;
                            border-radius: 10px 10px 0 0;
                            text-align: center;
                        }}
                        .content {{
                            background: #ffffff;
                            padding: 30px;
                            border: 1px solid #e0e0e0;
                            border-top: none;
                        }}
                        .info-section {{
                            background: #f8f9fa;
                            padding: 20px;
                            border-radius: 8px;
                            margin: 20px 0;
                        }}
                        .info-item {{
                            margin: 15px 0;
                            padding-bottom: 15px;
                            border-bottom: 1px solid #e0e0e0;
                        }}
                        .info-item:last-child {{
                            border-bottom: none;
                            padding-bottom: 0;
                        }}
                        .label {{
                            color: #667eea;
                            font-weight: 600;
                            font-size: 12px;
                            text-transform: uppercase;
                            letter-spacing: 0.5px;
                            margin-bottom: 5px;
                        }}
                        .value {{
                            color: #333;
                            font-size: 14px;
                            word-wrap: break-word;
                        }}
                        .message-box {{
                            background: #fff;
                            border-left: 4px solid #667eea;
                            padding: 15px;
                            margin-top: 10px;
                            border-radius: 4px;
                        }}
                        .footer {{
                            background: #f8f9fa;
                            padding: 20px;
                            border-radius: 0 0 10px 10px;
                            text-align: center;
                            font-size: 12px;
                            color: #666;
                        }}
                    </style>
                </head>
                <body>
                    <div class="header">
                        <h1 style="margin: 0; font-size: 24px;">📧 Nuevo Mensaje de Contacto</h1>
                        <p style="margin: 10px 0 0 0; opacity: 0.9;">Has recibido un nuevo mensaje desde el formulario de contacto</p>
                    </div>
                    <div class="content">
                        <div class="info-section">
                            <div class="info-item">
                                <div class="label">👤 Nombre Completo</div>
                                <div class="value">{serializer.data['name']}</div>
                            </div>
                            <div class="info-item">
                                <div class="label">📧 Correo Electrónico</div>
                                <div class="value"><a href="mailto:{serializer.data['email']}" style="color: #667eea; text-decoration: none;">{serializer.data['email']}</a></div>
                            </div>
                            <div class="info-item">
                                <div class="label">📱 Teléfono</div>
                                <div class="value">{serializer.data['phone']}</div>
                            </div>
                            <div class="info-item">
                                <div class="label">💬 Mensaje</div>
                                <div class="message-box">
                                    <div class="value">{serializer.data['message']}</div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="footer">
                        <p style="margin: 5px 0;">Este es un mensaje automático generado por el sistema de contacto.</p>
                        <p style="margin: 5px 0;">Por favor, responde al remitente a la brevedad posible.</p>
                    </div>
                </body>
                </html>
                """
                utilities.send_email(body, "Nuevo Mensaje de Contacto - Cookbook", os.getenv('CONTACT_NOTIFICATION_EMAIL'))
            except Exception as e:
                print(f"Error sending email: {e}")

            return JsonResponse(serializer.data, status=HTTPStatus.CREATED)
        return JsonResponse(serializer.errors, status=HTTPStatus.BAD_REQUEST)