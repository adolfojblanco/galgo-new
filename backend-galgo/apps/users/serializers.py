from rest_framework import serializers
from apps.users.models import User

# Users serializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role', 'password', 'is_active', 'is_staff']