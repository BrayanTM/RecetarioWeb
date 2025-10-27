from django.urls import path
from . import views

urlpatterns = [
    path('security/register/', views.SecurityRegisterView.as_view(), name='security_register'),
    path('security/verify/', views.SecurityVerifyView.as_view(), name='security_verify'),
    path('security/login/', views.SecurityLoginView.as_view(), name='security_login'),
]
