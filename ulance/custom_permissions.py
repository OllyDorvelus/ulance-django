from rest_framework import permissions


class MyUserPermissions(permissions.BasePermission):
    """
    Handles permissions for users.  The basic rules are

     - owner may GET, PUT, POST, DELETE
     - nobody else can access
     """

    def has_object_permission(self, request, view, obj):

        # check if user is owner
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.user

class MyAdminPermission(permissions.BasePermission):
    """
    Handles permissions for users.  The basic rules are

     - owner may GET, PUT, POST, DELETE
     - nobody else can access
     """

    def has_object_permission(self, request, view, obj):

        # check if user is owner
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser

