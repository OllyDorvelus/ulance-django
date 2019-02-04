from rest_framework import serializers
from orders.models import ServiceOrderModel, CartModel, EntryModel
from accounts.api.serializers import UserModelSerializer
from django.contrib.auth import get_user_model
from rest_framework.serializers import (
    ValidationError
)

User = get_user_model()


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryModel
        fields = '__all__'
        read_only_fields = ['days_remaining', 'is_ordered', 'order', 'cart', 'service', 'seller_notes']


class ServiceOwnerEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryModel
        fields = '__all__'
        read_only_fields = ['order', 'cart', 'service', 'buyer_notes']


class EntryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryModel
        fields = '__all__'

    def validate(self, data):
        return data

    def validate_order(self, value):
        data = self.get_initial()
        cart = data.get("")
        if cart is not None:
            raise ValidationError("Entry can not be apart of order and cart")

    def validate_cart(self, value):
        data = self.get_initial()
        order = data.get("order")
        if order is not None:
            raise ValidationError("Entry can not be apart of cart and order")
        return value


class ServiceOrderSerializer(serializers.ModelSerializer):
    order_entries = EntrySerializer(many=True)

    class Meta:
        model = ServiceOrderModel
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    cart_entries = EntrySerializer(many=True)

    class Meta:
        model = CartModel
        fields = '__all__'