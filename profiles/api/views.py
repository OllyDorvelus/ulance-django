from rest_framework import generics, permissions, mixins
from rest_framework.parsers import FileUploadParser
from .serializers import ( ProfileSerializer, SkillSerializer, LinkSerializer, PortfolioSerializer, LevelSerializer )
from profiles.models import ProfileModel, SkillModel, LinkModel, PortfolioModel, LevelModel
from ulance import pagination
from ulance.custom_permissions import MyUserPermissions
from django.contrib.auth import get_user_model

User = get_user_model()

#PROFILES
class ProfileListAPIView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = ProfileModel.objects.all()
    pagination_class = pagination.StandardResultsPagination

class ProfileUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = ProfileModel.objects.all()
    lookup_field = 'user__username'

class ProfileDetailAPIView(generics.RetrieveAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = ProfileSerializer
    queryset = ProfileModel.objects.all()
    lookup_field = 'user__username'
    permission_classes = [MyUserPermissions]
  #  parser_classes = [FileUploadParser]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)

#SKILLS
# class SkillListAPIView(generics.ListAPIView):
#     serializer_class = SkillSerializer
#     queryset = SkillModel.objects.all()

class SkillCreateAPIView(generics.CreateAPIView):
    serializer_class = SkillSerializer
    queryset = SkillModel.objects.all()
    permission_classes = [permissions.IsAdminUser]

class SkillDetailAPIView(generics.RetrieveAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = SkillSerializer
    queryset = SkillModel.objects.all()
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)

#LINKS
# class LinkListAPIView(generics.ListAPIView):
#     serializer_class = LinkSerializer
#     queryset = LinkModel.objects.all()

class LinkCreateAPIView(generics.CreateAPIView):
    serializer_class = LinkSerializer
    queryset = LinkModel.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer, *args, **kwargs):
        serializer.save(user=self.request.user)

class LinkDetailAPIView(generics.RetrieveAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = LinkSerializer
    queryset = LinkModel.objects.all()
    permission_classes = [MyUserPermissions]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)

class UserLinkListAPIView(generics.ListAPIView):
    serializer_class = LinkSerializer
    model = LinkModel.objects.all()
    pagination_class = pagination.StandardResultsPagination

    def get_queryset(self, *args, **kwargs):
        username = self.kwargs['user__username']
        user = User.objects.get(username=username)
        qs = LinkModel.objects.filter(user=user)
        return qs
#PORTFOLIOS

class PortfolioCreateAPIView(generics.CreateAPIView):
    serializer_class = PortfolioSerializer
    queryset = PortfolioModel.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer, *args, **kwargs):
        serializer.save(user=self.request.user)

class PortfolioDetailAPIView(generics.RetrieveAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = PortfolioSerializer
    queryset = PortfolioModel.objects.all()
    lookup_field = 'user__username'
    permission_classes = [MyUserPermissions]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)

#LEVELS

class LevelCreateAPIView(generics.CreateAPIView):
    serializer_class = LevelSerializer
    queryset = LevelModel.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer, *args, **kwargs):
        skill_name = serializer.validated_data['skill']
        skill = SkillModel.objects.get(name__iexact=skill_name)
        serializer.save(user=self.request.user, skill=skill)


class LevelDetailAPIView(generics.RetrieveAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = LevelSerializer
    queryset = LevelModel.objects.all()
    permission_classes = [MyUserPermissions]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)


class UserLevelListAPIView(generics.ListAPIView):
    serializer_class = LevelSerializer
    model = LevelModel.objects.all()
    pagination_class = pagination.StandardResultsPagination

    def get_queryset(self):
        username = self.kwargs['user__username']
        user = User.objects.get(username=username)
        qs = LevelModel.objects.filter(user=user)
        return qs



