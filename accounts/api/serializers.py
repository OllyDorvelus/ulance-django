__author__ = '13477'

from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import (
    EmailField,
    CharField,
    ValidationError
)
from profiles.models import ProfileModel

User = get_user_model()

class ProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = '__all__'

class UserModelSerializer(serializers.ModelSerializer):
    profile = ProfileModelSerializer(read_only=True)
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'profile'
        )

class UserCreateSerializer(serializers.ModelSerializer):
    email2 = EmailField()
    password2 = CharField(write_only=True)
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'email2',
            'password',
            'password2'
        )
        extra_kwargs = {"password":{"write_only": True}}

    def validate(self, data):
        # email = data['email']
        # user_qs = User.objects.filter(email=email)
        # if user_qs.exists():
        #     raise ValidationError("This User has already registered")
        return data

    def validate_email(self, value):
        data = self.get_initial()
        email1 = data.get("email2")
        email2 = value
        if not email2:
            raise ValidationError("This field may not be blank")
        if email1 != email2:
            raise ValidationError("Emails must match.")

        user_qs = User.objects.filter(email=email2)
        if user_qs.exists():
            raise ValidationError("This user has already registered.")

        return value

    def validate_email2(self, value):
        data = self.get_initial()
        email1 = data.get("email")
        email2 = value
        if email1 != email2:
            raise ValidationError("Emails must match.")
        return value

    def validate_password(self, value):
        data = self.get_initial()
        password = data.get("password2")
        password2 = value
        if password != password2:
            raise ValidationError("Passwords must match")
        return value

    def validate_password2(self, value):
        data = self.get_initial()
        password = data.get("password2")
        password2 = value
        if password != password2:
            raise ValidationError("Passwords must match")
        return value

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        new_user.save()
        new_profile = ProfileModel(user=new_user)
        new_profile.save()
        return validated_data

class UserLoginSerializer(serializers.ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField()
    email = EmailField(label='Email Address')
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'token',

        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                            }
    def validate(self, data):
        # email = data['email']
        # user_qs = User.objects.filter(email=email)
        # if user_qs.exists():
        #     raise ValidationError("This user has already registered.")
        return data

