from rest_framework import generics, permissions, mixins
from django.contrib.auth import get_user_model
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from ulance import pagination
from .serializers import ServiceOrderSerializer, CartSerializer, EntrySerializer, EntryCreateSerializer, ServiceOwnerEntrySerializer
from orders.models import ServiceOrderModel, EntryModel, CartModel
from django.shortcuts import get_object_or_404
from ulance.custom_permissions import EntryUserPermissions
from rest_framework.views import APIView

User = get_user_model()


class OrderListAPIView(generics.ListAPIView):
    serializer_class = ServiceOrderSerializer
    pagination_class = pagination.StandardResultsPagination
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        user = User.objects.get(pk=self.request.user.pk)
        qs = ServiceOrderModel.objects.filter(buyer=user)
        return qs


class CartDetailAPIView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    pagination_class = pagination.StandardResultsPagination
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, *args, **kwargs):
        user = User.objects.get(pk=self.request.user.pk)
        cart = get_object_or_404(CartModel, user=user)
        return cart


class EntryDetailAPIView(generics.RetrieveAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = EntrySerializer
    permission_classes = [permissions.IsAuthenticated, EntryUserPermissions]
    queryset = EntryModel.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)


class ServiceOwnerEntryDetailAPIView(generics.RetrieveAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
   # serializer_class = ServiceOwnerEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)


class AddEntryToCartAPIView(generics.CreateAPIView):
    serializer_class = EntryCreateSerializer
    permission_classes = [permissions.IsAuthenticated]






