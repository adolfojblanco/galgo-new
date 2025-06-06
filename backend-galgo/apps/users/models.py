from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('CUSTOMER', 'Comprador'),
        ('SELLER', 'Vendedor'),
        ('ADMIN', 'Administrador'),
        ('DRIVER', 'Conductor')
    )

    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True, blank=False)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100)
    role = models.CharField(choices=ROLE_CHOICES, blank=False, default='CUSTOMER', max_length=15)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    objects = UserManager()

    def has_role(self, role_name):
        return self.role == role_name

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


