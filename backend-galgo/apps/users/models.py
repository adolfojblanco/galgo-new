from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('USER', 'Usuario'),
        ('ADMIN', 'Administrador'),
        ('REST', 'Restaurante'),
        ('DRIVER', 'Conductor')
    )

    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True, blank=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(choices=ROLE_CHOICES, blank=False, default='USER', max_length=8)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
