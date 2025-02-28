from django.contrib import admin
from .models import RestaurantCategory, RestaurantAddress, Restaurant

# Register your models here.
admin.site.register(RestaurantCategory)

admin.site.register(RestaurantAddress)

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'mobile_phone', 'email')