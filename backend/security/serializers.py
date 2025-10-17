from rest_framework import serializers
from .models import UsersMetadata

class UsersMetadataSerializer(serializers.ModelSerializer):


    class Meta:
        model = UsersMetadata
        fields = ['user', 'token']
        extra_kwargs = {
            'user': {'required': True, 'allow_blank': False},
            'token': {'required': True, 'max_length': 255, 'allow_blank': False},
        }
