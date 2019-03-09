from rest_framework import generics, permissions, mixins
from django.contrib.auth import get_user_model
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from ulance import pagination
from .serializers import ( ServiceOrderSerializer, ServiceOrderCreateSerializer, CartSerializer,
                           EntrySerializer, EntryCreateSerializer, ServiceOwnerEntrySerializer, ComplaintSerializer, EntryServiceOrderSerializer )
from orders.models import ServiceOrderModel, EntryModel, CartModel, ComplaintModel
from services.models import ServiceModel
from django.shortcuts import get_object_or_404
from ulance.custom_permissions import EntryUserPermissions, EntryServiceUserPermissions, ComplaintUserPermissions
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q


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
    serializer_class = ServiceOrderCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.request.user
        cart = user.cart
        entries = cart.cart_entries.all()
        serializer.validated_data['buyer'] = user
        serializer.validated_data['paid'] = cart.total
        if not entries:
            return Response({'message': "Cart is empty, please add at least one service."})
        new_order = self.perform_create(serializer)
        for entry in entries:
            entry.is_ordered = True
            entry.order = new_order
            entry.save()
        cart.clear_cart()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()


class ServiceOrderListAPIView(generics.ListAPIView):
    serializer_class = EntryServiceOrderSerializer
    pagination_class = pagination.StandardResultsPagination
    permission_classes = [permissions.IsAuthenticated, EntryServiceUserPermissions]

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        valid_status = ['ORD', 'INP']
        qs = EntryModel.objects.filter(service__user=user, is_ordered=True, status__in=valid_status)
        return qs


class ServiceOrderCompleteListAPIView(generics.ListAPIView):
    serializer_class = EntryServiceOrderSerializer
    pagination_class = pagination.StandardResultsPagination
    permission_classes = [permissions.IsAuthenticated, EntryServiceUserPermissions]

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        valid_status = ['COM']
        qs = EntryModel.objects.filter(service__user=user, is_ordered=True, status__in=valid_status)
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
    permission_classes = [permissions.IsAuthenticated, EntryServiceUserPermissions]
    queryset = EntryModel.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)


class AddEntryToCartAPIView(generics.CreateAPIView):
    serializer_class = EntryCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'service_id'

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.request.user
        cart = CartModel.objects.get(user=user)
        service_id = self.kwargs['service_id']
        service = get_object_or_404(ServiceModel, pk=service_id)

        if service.user == user:
            return Response({"message": "Can't add your own services to cart"}, status=status.HTTP_400_BAD_REQUEST)

        if cart.cart_entries.filter(service=service).exists():
                return Response({"message": "Service already in cart"}, status=status.HTTP_400_BAD_REQUEST)

        serializer.validated_data['cart'] = cart
        serializer.validated_data['service'] = service
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer, *args, **kwargs):
        serializer.save()


class ComplaintDetailAPIView(generics.RetrieveAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = ComplaintSerializer
    queryset = ComplaintModel
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)


class ComplaintCreateAPIView(generics.CreateAPIView):
    serializer_class = ComplaintSerializer
    permission_classes = [permissions.IsAuthenticated, ComplaintUserPermissions]
    lookup_field = 'entry_id'

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.request.user
        entry_id = self.kwargs['entry_id']
        entry = get_object_or_404(EntryModel, pk=entry_id)
        if entry.status != 'COM':
            return Response({"message": "Entry need to be marked as completed before filing a complaint."},
                            status=status.HTTP_400_BAD_REQUEST)
        if entry.order.buyer != user:
            return Response({"message": "You do not have permission to file a complaint on this entry"},
                            status=status.HTTP_401_UNAUTHORIZED)
        serializer.validated_data['entry'] = entry
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer, *args, **kwargs):
        serializer.save()







