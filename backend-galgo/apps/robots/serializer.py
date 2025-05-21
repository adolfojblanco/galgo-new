from rest_framework import serializers
from apps.robots.models import Robot

class RobotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Robot
        fields = ['name', 'model', 'battery_level', 'status', 'is_active']