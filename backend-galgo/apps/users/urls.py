from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CustomTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.users.views import UserApiviewSet

router_user = DefaultRouter()
router_user.register(
    prefix='', basename='users', viewset = UserApiviewSet
)

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]