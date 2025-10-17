from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UsersMetadata(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    token = models.CharField(max_length=255)


    def __str__(self):
        return f"Metadata for {self.user.username}"


    class Meta:
        db_table = 'users_metadata'
        verbose_name = 'User Metadata'
        verbose_name_plural = 'Users Metadata'
