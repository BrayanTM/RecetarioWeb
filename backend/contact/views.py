from rest_framework.views import APIView
from django.http import JsonResponse
from http import HTTPStatus
from .serializers import ContactMessageSerializer
from utilities import utilities
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


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
                <h2>New Contact Message</h2>
                <ul>
                    <li><strong>Name:</strong> {serializer.data['name']}</li>
                    <li><strong>Email:</strong> {serializer.data['email']}</li>
                    <li><strong>Phone:</strong> {serializer.data['phone']}</li>
                    <li><strong>Message:</strong> {serializer.data['message']}</li>
                </ul>
                """
                utilities.send_email(body, "New Contact Message", serializer.data['email'])
            except Exception as e:
                print(f"Error sending email: {e}")

            return JsonResponse(serializer.data, status=HTTPStatus.CREATED)
        return JsonResponse(serializer.errors, status=HTTPStatus.BAD_REQUEST)