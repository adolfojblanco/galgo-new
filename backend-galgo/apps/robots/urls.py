from rest_framework.routers import DefaultRouter
from .views import RobotApiView

"""
    Robots Urls
"""

router_robots = DefaultRouter()

router_robots.register('', basename='robots', viewset=RobotApiView)

