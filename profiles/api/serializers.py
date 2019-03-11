from profiles.models import (ProfileModel, SkillModel, PictureModel, LinkModel, CertificationModel, EducationModel, MajorModel, SchoolModel)
from rest_framework import serializers
from django.contrib.auth import get_user_model
from accounts.api.serializers import UserModelSerializer

User = get_user_model()

# from drf_extra_fields.fields import Base64ImageField
#
# class UploadedBase64ImageSerializer(serializers.Serializer):
#     file = Base64ImageField(required=False)
#     created = serializers.DateTimeField()


class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension

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
    profile_pic = Base64ImageField(read_only=True)
    url = serializers.SerializerMethodField()

    class Meta:
        model = ProfileModel
        fields = '__all__'

    def get_url(self, obj):
        return obj.get_absolute_url()


class ProfilePictureSerializer(serializers.ModelSerializer):
    user = UserModelSerializer(read_only=True)
    profile_pic = Base64ImageField()

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
    pass
    # user = UserModelSerializer(read_only=True)
    #
    # class Meta:
    #     model = PortfolioModel
    #     fields = '__all__'


# class LevelSerializer(serializers.ModelSerializer):
#     user = UserModelSerializer(read_only=True)
#     skill = serializers.ChoiceField(choices=list(SkillModel.objects.all().values_list('name', flat=True)))
#
#     class Meta:
#         model = LevelModel
#         fields = '__all__'
#         read_only_fields = ['user']
#
#     def update(self, instance, validated_data):
#         skill_name = validated_data['skill']
#         skill = SkillModel.objects.get(name__iexact=skill_name)
#         instance.skill = skill
#         instance.skill_level = validated_data.get('skill_level', instance.skill_level)
#         instance.save()
#         return instance


class CertificationSerializer(serializers.ModelSerializer):
    user = UserModelSerializer(read_only=True)

    class Meta:
        model = CertificationModel
        fields = '__all__'

# EDUCATION


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolModel
        fields = '__all__'


class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = MajorModel
        fields = '__all__'


class EducationSerializer(serializers.ModelSerializer):
    user = UserModelSerializer(read_only=True)
    school = serializers.ChoiceField(choices=list(SchoolModel.objects.all().order_by('name').values_list('name', flat=True)))
    major = serializers.ChoiceField(choices=list(MajorModel.objects.all().order_by('name').values_list('name', flat=True)))

    class Meta:
        model = EducationModel
        fields = '__all__'
        read_only_fields = ['user']

    def update(self, instance, validated_data):
        school_name = validated_data.get('school')
        major_name = validated_data.get('major')
        school = SchoolModel.objects.get(name__iexact=school_name)
        major = MajorModel.objects.get(name__iexact=major_name)
        instance.school = school
        instance.major = major
        instance.degree_type = validated_data.get('degree_type', instance.degree_type)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance








