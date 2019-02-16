from rest_framework.serializers import (
    EmailField,
    CharField,
    ValidationError
)
from rest_framework import serializers
from services.models import ServiceModel, CategoryModel, ReviewModel, ServicePictureModel
from django.contrib.auth import get_user_model
from accounts.api.serializers import UserModelSerializer
from django.db.models import Count, Avg, Value
from django.db.models import Sum

User = get_user_model()


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryModel
        fields = '__all__'


class ServicePhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServicePictureModel
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    user = UserModelSerializer(read_only=True)
    photos = ServicePhotoSerializer(many=True)
    url = serializers.SerializerMethodField()
  #  category = CategorySerializer(many=True)

    class Meta:
        model = ServiceModel
        fields = '__all__'

    def get_url(self, obj):
        return obj.get_absolute_url()


class ServiceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceModel
        fields = '__all__'
        read_only_fields = ['user']


class ReviewSerializer(serializers.ModelSerializer):
    user = UserModelSerializer(read_only=True)
    service = ServiceSerializer(read_only=True)

    class Meta:
        model = ReviewModel
        fields = '__all__'





