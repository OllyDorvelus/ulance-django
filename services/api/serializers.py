from rest_framework.serializers import (
    EmailField,
    CharField,
    ValidationError
)
from rest_framework import serializers
from services.models import ServiceModel, CategoryModel
from django.contrib.auth import get_user_model
from accounts.api.serializers import UserModelSerializer
User = get_user_model()

class ServiceSerializer(serializers.ModelSerializer):
    user = UserModelSerializer(read_only=True)
    class Meta:
        model = ServiceModel
        fields = '__all__'
        read_only_fields = ['buyer']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'
