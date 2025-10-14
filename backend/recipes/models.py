from django.db import models
from autoslug import AutoSlugField
from categories.models import Category


# Create your models here.
class Recipe(models.Model):
    category = models.ForeignKey(Category, models.DO_NOTHING, null=False)
    name = models.CharField(max_length=100, null=False, unique=True)
    slug = AutoSlugField(populate_from='name', max_length=100, unique=True, null=False)
    time = models.CharField(max_length=100, null=True)
    picture = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'recipes'
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'