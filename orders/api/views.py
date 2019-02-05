from rest_framework import generics, permissions, mixins
from django.contrib.auth import get_user_model
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from ulance import pagination
from .serializers import ServiceOrderSerializer, CartSerializer, EntrySerializer, EntryCreateSerializer, ServiceOwnerEntrySerializer
from orders.models import ServiceOrderModel, EntryModel, CartModel
from services.models import ServiceModel
from django.shortcuts import get_object_or_404
from ulance.custom_permissions import EntryUserPermissions, EntryServiceUserPermissions
from rest_framework.response import Response
from rest_framework import status


User = get_user_model()


class OrderListAPIView(generics.ListAPIView):
    serializer_class = ServiceOrderSerializer
    pagination_class = pagination.StandardResultsPagination
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        qs = ServiceOrderModel.objects.filter(buyer=user)
        return qs


class OrderCreateAPIView(generics.CreateAPIView):
    pass


class ServiceOrderListAPIView(generics.ListAPIView):
    serializer_class = EntrySerializer
    pagination_class = pagination.StandardResultsPagination
    permission_classes = [permissions.IsAuthenticated, EntryServiceUserPermissions]

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        qs = EntryModel.objects.filter(service__user=user, is_ordered=True)
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


class ServiceOwnerEntryDetailAPIView(generics.RetrieveAPIView, mixins.UpdateModelMixin):
    serializer_class = ServiceOwnerEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)


class AddEntryToCartAPIView(generics.CreateAPIView):
    serializer_class = EntryCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'

    def create(self, request, *args, **kwargs):
        user = self.request.user
        cart = CartModel.objects.get(user=user)
        service_id = self.kwargs['pk']
        service = get_object_or_404(ServiceModel, pk=service_id)
        if service.user == user:
            return Response({"message": "Can't add your own services to cart"}, status=status.HTTP_400_BAD_REQUEST)
        for entry in cart.cart_entries.all():
            if entry.service == service:
                return Response({"message": "Service already in cart"}, status=status.HTTP_400_BAD_REQUEST)
        return super(AddEntryToCartAPIView, self).create(request, *args, **kwargs)

    def perform_create(self, serializer, *args, **kwargs):
        user = self.request.user
        cart = CartModel.objects.get(user=user)
        service_id = self.kwargs['pk']
        service = get_object_or_404(ServiceModel, pk=service_id)
        serializer.save(cart=cart, service=service)







