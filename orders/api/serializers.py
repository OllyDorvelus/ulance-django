from rest_framework import serializers
from orders.models import ServiceOrderModel, CartModel, EntryModel
from accounts.api.serializers import UserModelSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryModel
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceOrderModel
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    entry = EntrySerializer(many=True)

    class Meta:
        model = CartModel
        fields = '__all__'