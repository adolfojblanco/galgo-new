from rest_framework.viewsets import  ModelViewSet
from .serializer import RobotSerializer
from .models import Robot

"""
    ROBOTS VIEWS
"""

class RobotApiView(ModelViewSet):
    serializer_class = RobotSerializer
    queryset = Robot.objects.all()