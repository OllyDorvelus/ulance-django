from rest_framework.serializers import (
    EmailField,
    CharField,
    ValidationError
)
from rest_framework import serializers
from services.models import ServiceModel, CategoryModel, JobModel, ServicePictureModel
from django.contrib.auth import get_user_model
from accounts.api.serializers import UserModelSerializer
from django.db.models import Count, Avg, Value
from django.db.models import Sum

User = get_user_model()


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.ModelField(model_field=CategoryModel()._meta.get_field('id'))

    class Meta:
        model = CategoryModel
        fields = '__all__'


class ServicePhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServicePictureModel
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    user = UserModelSerializer(read_only=True)
    photos = ServicePhotoSerializer(many=True, read_only=True)
    url = serializers.SerializerMethodField()
    category = CategorySerializer(many=True, read_only=True)
    delivery_time_display = serializers.SerializerMethodField()

    class Meta:
        model = ServiceModel
        fields = '__all__'
        read_only_fields = ['average_rating', 'purchases']

    def get_url(self, obj):
        return obj.get_absolute_url()

    def get_delivery_time_display(self, obj):
        if obj.delivery_time == 'Normal':
            return "3-5"
        if obj.delivery_time == 'Later':
            return '7+'
        if obj.delivery_time == 'Early':
            return '1-3'


class ServiceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceModel
        fields = '__all__'
        read_only_fields = ['user', 'purchases', 'average_rating']








