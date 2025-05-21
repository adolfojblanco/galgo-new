from django.contrib import admin
from .models import StoreCategory, Store
from apps.users.models import User

# Register your models here.

@admin.register(StoreCategory)
class StoreCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display  = ['id', 'name', 'owner']