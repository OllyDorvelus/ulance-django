from rest_framework.serializers import (
    EmailField,
    CharField,
    ValidationError
)
from rest_framework import serializers
from services.models import ServiceModel, CategoryModel, JobModel, ServicePictureModel
from django.contrib.auth import get_user_model
from accounts.api.serializers import UserModelSerializer
from profiles.api.serializers import SkillSerializer
from django.utils.timesince import timesince
from django.db.models import Count, Avg, Value
from django.db.models import Sum

User = get_user_model()


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.ModelField(model_field=CategoryModel()._meta.get_field('id'))

    class Meta:
        model = CategoryModel
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    user = UserModelSerializer(read_only=True)
    freelancer = UserModelSerializer(read_only=True)
    url = serializers.SerializerMethodField()
    categories = CategorySerializer(many=True, read_only=True)
    skills = SkillSerializer(many=True, read_only=True)
    timesince = serializers.SerializerMethodField()
    status_display = serializers.SerializerMethodField()


    class Meta:
        model = JobModel
        fields = '__all__'
        read_only_fields = ['status', 'freelancer']


    def get_url(self, obj):
        return obj.get_absolute_url()

    def get_status_display(self, obj):
        if obj.status == 'NT':
            return 'Not Taken'
        elif obj.status == 'T':
            return "Taken"
        else:
            return ''

    def get_timesince(self, obj):
        return f'{timesince(obj.created_at)} days ago'


class JobCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobModel
        fields = '__all__'
        read_only_fields = ['status', 'freelancer']


class ServicePhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServicePictureModel
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    user = UserModelSerializer(read_only=True)
    photos = ServicePhotoSerializer(many=True, read_only=True)
    url = serializers.SerializerMethodField()
    categories = CategorySerializer(many=True, read_only=True)
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








