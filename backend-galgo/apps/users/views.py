from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from apps.users.models import User
from apps.users.serializers import UserSerializer

# Users views.

class UserApiviewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all()
