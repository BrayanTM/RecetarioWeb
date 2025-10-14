from rest_framework import serializers
from .models import Recipe
from categories.models import Category
from dotenv import load_dotenv
import os


class RecipeSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    created_at = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)
    picture_url = serializers.SerializerMethodField(read_only=True)
    picture = serializers.CharField(max_length=100, required=False, allow_blank=True, allow_null=True)


    class Meta:
        model = Recipe
        fields = ['id', 'name', 'slug', 'time', 'description', 'created_at', 'category', 'category_name', 'picture', 'picture_url']
        read_only_fields = ['slug', 'created_at']


    def get_picture_url(self, obj):
        if obj.picture:
            return f"{os.getenv('BASE_URL')}uploads/recipes/{obj.picture}"
        return None