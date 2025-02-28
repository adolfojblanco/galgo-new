from django.db import models
from applications.users.models import User
from applications.base.models import BaseModel
from simple_history.models import HistoricalRecords

""" Model for restaurant category """
class RestaurantCategory(BaseModel):
    name = models.CharField('Nombre Categoria', max_length=80, null=False, blank=False, unique=True)
    state = models.BooleanField('Activo', default=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.name


""" Model for restaurant """
class Restaurant(BaseModel):
    name = models.CharField('Nombre Restaurante', max_length=100, null=False, blank=False, unique=True)
    local_phone = models.CharField('Número Fijo', max_length=20, null=True, blank=True, unique=True)
    mobile_phone = models.CharField('Número Móvil', max_length=20, null=True, blank=True, unique=True)
    email = models.EmailField(blank=True, max_length=100, unique=True)
    logo = models.ImageField('Logo Restaurante', upload_to='restaurantes/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Encargado', null=False, blank=False)
    state = models.BooleanField('Activo', default=True)
    category = models.ForeignKey(
        RestaurantCategory, on_delete=models.CASCADE, verbose_name= 'Categoria' ,null=False, blank=False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "Restaurant"
        verbose_name_plural = "Restaurantes"
        ordering = ('name',)

    def __str__(self):
        return self.name


""" Model address for restaurant """
class RestaurantAddress(BaseModel):
    street = models.CharField('Calle', max_length=100, null=False, blank=False, unique=False)
    number = models.CharField('Número', max_length=100, null=False, blank=False, unique=False)
    floor = models.CharField('Piso', max_length=100, null=False, blank=False, unique=True)
    door = models.CharField('Puerta', max_length=100, null=False, blank=False, unique=True)
    town = models.CharField('Población', max_length=100, null=False, blank=False, unique=False)
    postal_code = models.IntegerField('Código Postal', null=False, blank=False, unique=False)
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, verbose_name= 'Restaurante' ,null=False, blank=False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "Dirección"
        verbose_name_plural = "Direcciones"

    def __str__(self):
        return f'Restaurante {self.restaurant}, {self.street}'