from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False)
    slug = AutoSlugField(populate_from='name', unique=True, null=False)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'