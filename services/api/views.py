from rest_framework import generics, permissions, mixins
from .serializers import ( ServiceSerializer, CategorySerializer )
from services.models import ServiceModel, CategoryModel
from ulance import pagination
from ulance.custom_permissions import MyUserPermissions, MyAdminPermission
from django.contrib.auth import get_user_model

User = get_user_model()

class ServiceListAPIView(generics.ListAPIView):
    serializer_class = ServiceSerializer
    queryset = ServiceModel.objects.all()
    pagination_class = pagination.StandardResultsPagination

class ServiceCreateAPIView(generics.CreateAPIView):
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer, *args, **kwargs):
        serializer.save(user=self.request.user)

class ServiceDetailAPIView(generics.RetrieveAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = ServiceSerializer
    queryset = ServiceModel.objects.all()
    permission_classes = [MyUserPermissions]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)

class UserServiceListAPIView(generics.ListAPIView):
    serializer_class = ServiceSerializer
    pagination_class = pagination.StandardResultsPagination

    def get_queryset(self, *args, **kwargs):
        username = self.kwargs['user__username']
        user = User.objects.get(username=username)
        qs = ServiceModel.objects.filter(user=user)
        return qs

class CategoryListAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = CategoryModel.objects.all()
    pagination_class = pagination.StandardResultsPagination

class CategoryCreateAPIView(generics.CreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]

class CategoryDetailAPIView(generics.RetrieveAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = CategorySerializer
    queryset = CategoryModel.objects.all()
    permission_classes = [MyAdminPermission]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)




