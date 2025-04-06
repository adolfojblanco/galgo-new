from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.
class User(AbstractBaseUser):

    ROLE_CHOICES = (
        ('USER', 'Usuario'),
        ('ADMIN', 'Administrador'),
        ('REST', 'Restaurante'),
        ('DRIVER', 'Conductor')
    )

    role = models.CharField(choices=ROLE_CHOICES, blank=False, default='USER', max_length=8)

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
