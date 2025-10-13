from django.urls import path
from . import views

urlpatterns = [
    path('example', views.ClassExample.as_view(), name='example'),
    path('example/<int:id>', views.ClassExampleParams.as_view(), name='example_params'),
    path('example-upload', views.FileUploadExample.as_view(), name='example_upload'),
]