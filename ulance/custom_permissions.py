from rest_framework import permissions
from orders.models import CartModel
from django.contrib.auth import get_user_model

User = get_user_model()


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


class StrictUserPermissions(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user or request.user.is_superuser


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


class EntryUserPermissions(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if obj.is_ordered:
            return False
        return obj.cart.user == request.user


class EntryServiceUserPermissions(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if obj.is_ordered:
            return obj.service.user == request.user
        return False


class ComplaintUserPermissions(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if request.method in permissions.SAFE_METHODS:
            if obj.entry.service.user == request.user:
                return True
        if obj.entry.order.buyer == request.user:
            return True
        return False


