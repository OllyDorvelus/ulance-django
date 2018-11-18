from rest_framework.serializers import (
    EmailField,
    CharField,
    ValidationError
)
from rest_framework import serializers
from services.models import ServiceModel, CategoryModel, ReviewModel
from django.contrib.auth import get_user_model
from accounts.api.serializers import UserModelSerializer
from django.db.models import Count, Avg, Value
from django.db.models import Sum

User = get_user_model()

class ServiceSerializer(serializers.ModelSerializer):
    user = UserModelSerializer(read_only=True)
    avg_rate = serializers.SerializerMethodField()
    purchases = serializers.SerializerMethodField()

    class Meta:
        model = ServiceModel
        fields = '__all__'

    def get_avg_rate(self, obj):
        return obj.avg_rate

    def get_purchases(self, obj):
        return obj.purchases

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryModel
        fields = '__all__'



class ReviewSerializer(serializers.ModelSerializer):
    user = UserModelSerializer(read_only=True)
    class Meta:
        model = ReviewModel
        fields = '__all__'
