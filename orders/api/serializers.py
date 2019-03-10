from rest_framework import serializers
from orders.models import ServiceOrderModel, ComplaintModel
from services.api.serializers import ServiceSerializer
from accounts.api.serializers import UserModelSerializer
from django.contrib.auth import get_user_model
from services.api.serializers import ServiceSerializer
from rest_framework.serializers import (
    ValidationError
)

User = get_user_model()


# class EntrySerializer(serializers.ModelSerializer):
#     service = ServiceSerializer(read_only=True)
#
#     class Meta:
#         model = EntryModel
#         fields = '__all__'
#         read_only_fields = ['days_remaining', 'is_ordered', 'order', 'cart', 'service', 'seller_notes', 'status',
#                             'is_delivered']


class ServiceOrderSerializer(serializers.ModelSerializer):
    buyer = UserModelSerializer(read_only=True)

    class Meta:
        model = ServiceOrderModel
        fields = '__all__'


# class EntryServiceOrderSerializer(serializers.ModelSerializer):
#     service = ServiceSerializer(read_only=True)
#     order = ServiceOrderUserSerializer(read_only=True)
#
#     class Meta:
#         model = EntryModel
#         fields = '__all__'
#         read_only_fields = ['days_remaining', 'is_ordered', 'order', 'cart', 'service', 'seller_notes', 'status',
#                             'is_delivered']


# class ServiceOwnerEntrySerializer(serializers.ModelSerializer):
#     service = ServiceSerializer(read_only=True)
#
#     class Meta:
#         model = EntryModel
#         exclude = ('cart',)
#         read_only_fields = ['order', 'cart', 'service', 'buyer_notes', 'is_delivered', 'quantity']


# class EntryCreateSerializer(serializers.ModelSerializer):
#     service = ServiceSerializer(read_only=True)
#
#     class Meta:
#         model = EntryModel
#         fields = '__all__'
#         read_only_fields = ['seller_notes', 'days_remaining', 'is_ordered', 'status', 'service', 'order', 'cart', 'quantity', 'buyer_notes', 'is_delivered']
#
#     def validate(self, data):
#         return data
#
#     def validate_order(self, value):
#         data = self.get_initial()
#         cart = data.get("")
#         if cart is not None:
#             raise ValidationError("Entry can not be apart of order and cart")
#
#     def validate_cart(self, value):
#         data = self.get_initial()
#         order = data.get("order")
#         if order is not None:
#             raise ValidationError("Entry can not be apart of cart and order")
#         return value


# class ServiceOrderSerializer(serializers.ModelSerializer):
#     pass
#   #  order_entries = EntrySerializer(many=True, read_only=True)
#
#     class Meta:
#         model = ServiceOrderModel
#         fields = '__all__'


class ServiceOrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceOrderModel
        fields = '__all__'
        read_only_fields = ['buyer', 'paid', 'status', 'service', 'job']


class JobOrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceOrderModel
        fields = '__all__'
        read_only_fields = ['buyer', 'status', 'paid', 'service', 'job']


# class CartSerializer(serializers.ModelSerializer):
#     cart_entries = EntrySerializer(many=True)
#
#     class Meta:
#         model = CartModel
#         fields = '__all__'


class ComplaintSerializer(serializers.ModelSerializer):
  #  entry = EntrySerializer(read_only=True)

    class Meta:
        model = ComplaintModel
        fields = '__all__'
        read_only_fields = ['is_valid_complaint']