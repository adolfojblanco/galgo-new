from django.db import models
from apps.users.models import User

# Create your models here.
class ClassModel(models.Model):
    """Details for models"""
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_creator = models.ForeignKey(User, on_delete=models.CASCADE)
    user_editor = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract = True