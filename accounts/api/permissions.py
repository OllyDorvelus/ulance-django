from rest_framework import permissions

class UserCreatePermission(permissions.BasePermission):
    def has_permission(self, request, view):
            if request.user.is_authenticated and not request.user.is_superuser:
                return False
            return True
