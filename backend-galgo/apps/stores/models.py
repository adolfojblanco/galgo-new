from django.db import models
from apps.users.models import User

# Create your models here.

class StoreCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        super(StoreCategory, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Store(models.Model):
    owner = models.ForeignKey(User, verbose_name='Propietario' ,on_delete=models.CASCADE, related_name='stores')
    name = models.CharField(verbose_name='Nombre', max_length=100, blank=False, null=False)
    description = models.TextField('Descripción', blank=True)
    category = models.ForeignKey(StoreCategory, verbose_name='Categoria' ,on_delete=models.SET_NULL, null=True)
    logo = models.ImageField(upload_to='store_logos', null=True, blank=True)
    delivery_radius = models.FloatField('Radio de Entrega', blank=False, null=False, default=0.00)
    minimum_order = models.DecimalField('Orden Mínima', max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tienda'
        verbose_name_plural = 'Tiendas'