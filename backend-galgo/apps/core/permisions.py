from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.rol == "ADMIN":
            return True
        else:
            return False

class IsDriver(BasePermission):
    def has_permission(self, request, view):
        if request.user.rol == "DRIVER":
            return True
        else:
            return False


class IsRestaurant(BasePermission):
    def has_permission(self, request, view):
        if request.user.rol == "RESTAURANT":
            return True
        else:
            return False