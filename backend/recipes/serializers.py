from rest_framework import serializers
from .models import Recipe
from categories.models import Category
import cloudinary
import cloudinary.utils


class RecipeSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    user_name = serializers.ReadOnlyField(source='user.username')
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)
    picture_url = serializers.SerializerMethodField(read_only=True)
    picture = serializers.CharField(max_length=100, required=False, allow_blank=True, allow_null=True)


    class Meta:
        model = Recipe
        fields = ['id', 'name', 'slug', 'time', 'description', 'created_at', 'category', 'category_name', 'picture', 'picture_url', 'user', 'user_name']
        read_only_fields = ['id', 'slug', 'created_at', 'user', 'user_name']


    def get_picture_url(self, obj):
        if obj.picture:
            # Generar URL segura desde Cloudinary
            return cloudinary.utils.cloudinary_url(obj.picture)[0]
        return None
