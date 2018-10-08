__author__ = '13477'
from profiles.models import (ProfileModel, SkillModel, PortfolioModel, PictureModel, LinkModel, LevelModel, CertificationModel)
from rest_framework import serializers
from services.api.serializers import ServiceSerializer
from rest_framework.serializers import (
    EmailField,
    CharField,
    ValidationError
)
from django.contrib.auth import get_user_model
User = get_user_model()
from accounts.api.serializers import UserModelSerializer

# class UserModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = (
#             'id',
#             'username',
#             'email',
#         )

class ProfileSerializer(serializers.ModelSerializer):
    user = UserModelSerializer(read_only=True)
    class Meta:
        model = ProfileModel
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillModel
        fields = '__all__'

class LinkSerializer(serializers.ModelSerializer):
    user = UserModelSerializer(read_only=True)
    class Meta:
        model = LinkModel
        fields = '__all__'
       # read_only_fields = ['user']

class PortfolioSerializer(serializers.ModelSerializer):
    user = UserModelSerializer(read_only=True)
    class Meta:
        model = PortfolioModel
        fields = '__all__'

class LevelSerializer(serializers.ModelSerializer):
    user = UserModelSerializer(read_only=True)
  #  skill = SkillSerializer(read_only=True)
    skill = serializers.ChoiceField(choices=list(SkillModel.objects.all().values_list('name', flat=True)))
    class Meta:
        model = LevelModel
        fields = '__all__'
        read_only_fields = ['user']

class CertificationSerializer(serializers.ModelSerializer):
    user = UserModelSerializer(read_only=True)
    class Meta:
        model = CertificationModel
        fields = '__all__'



