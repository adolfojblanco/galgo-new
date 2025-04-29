from django.contrib import admin
from .models import Robot

@admin.register(Robot)
class RobotsAdmin(admin.ModelAdmin):
    list_display  = ['id', 'name', 'model', 'status', 'is_active']
    readonly_fields = ['user_creator', 'user_editor']

    def save_model(self, request, obj, form, change):
        user_creator = request.user
        obj.user_creator = user_creator
        obj.save()
        super().save_model(request, obj, form, change)