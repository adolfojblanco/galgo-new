from django.contrib import admin
from .models import User, UserBusiness

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(UserBusiness)
class UserBusiness(admin.ModelAdmin):
    pass

