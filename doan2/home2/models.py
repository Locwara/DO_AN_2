from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=254, unique=True   )
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='home_user_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        related_name='home_user_permissions',
        blank=True
    )
    class Meta:
        db_table = 'auth_user'