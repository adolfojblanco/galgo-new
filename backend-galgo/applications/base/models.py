from django.db import models

# Create your models here.
class BaseModel(models.Model):
    state = models.BooleanField('Estado', default=True)
    create_at = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)
    modified_at = models.DateField('Fecha de Edición', auto_now=True, auto_now_add=False)
    deleted_at = models.DateField('Fecha de Eliminación', auto_now=True, auto_now_add=False)


    class Meta:
        abstract = True
        verbose_name: "Modelo Base"
        verbose_name_plural: "Modelo Base"

