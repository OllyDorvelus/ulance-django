from rest_framework import generics, permissions, mixins
from .serializers import ( ServiceSerializer, CategorySerializer, ReviewSerializer, ServiceCreateSerializer )
from services.models import ServiceModel, CategoryModel, ReviewModel
from ulance import pagination
from ulance.custom_permissions import MyUserPermissions, MyAdminPermission
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ServiceFilter
from rest_framework.filters import OrderingFilter

User = get_user_model()

# SERVICES


class ServiceListAPIView(generics.ListAPIView):
    serializer_class = ServiceSerializer
    queryset = ServiceModel.objects.all()
    pagination_class = pagination.StandardResultsPagination
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ("price", "avg_rate_sort", "purchases_sort")
    filterset_class = ServiceFilter


class ServiceCreateAPIView(generics.CreateAPIView):
    serializer_class = ServiceCreateSerializer
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


class ServiceReviewListAPIView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    pagination_class = pagination.StandardResultsPagination

    def get_queryset(self, *args, **kwargs):
        pk = self.kwargs['pk']
        service = ServiceModel.objects.get(pk=pk)
        qs = ReviewModel.objects.filter(service=service)
        return qs

# CATEGORIES


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

# REVIEWS


class ReviewCreateAPIView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permissions_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer, *args, **kwargs):
        service_id = self.kwargs['pk']
        service = ServiceModel.objects.get(pk=service_id)
        serializer.save(service=service, user=self.request.user)


class ReviewDetailAPIView(generics.RetrieveAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = ReviewSerializer
    queryset = ReviewModel.objects.all()
    permission_classes = [MyUserPermissions]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)




