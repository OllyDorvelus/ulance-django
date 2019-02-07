from rest_framework import generics, permissions, mixins
from rest_framework.parsers import FileUploadParser
from .serializers import ( ProfileSerializer, SkillSerializer, LinkSerializer, PortfolioSerializer, LevelSerializer, CertificationSerializer, ProfilePictureSerializer, EducationSerializer, MajorSerializer,
SchoolSerializer)
from profiles.models import ProfileModel, SkillModel, LinkModel, PortfolioModel, LevelModel, CertificationModel, EducationModel, MajorModel, SchoolModel
from ulance import pagination
from ulance.custom_permissions import MyUserPermissions, MyAdminPermission
from django.contrib.auth import get_user_model
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .filters import MajorFilter, SkillFilter, SchoolFilter, ProfileFilter

User = get_user_model()

# PROFILES


class ProfileListAPIView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    pagination_class = pagination.StandardResultsPagination
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ['user__username', 'services_completed', 'first_name', 'last_name']
    # filterset_class = ProfileFilter

    def get_queryset(self, *args, **kwargs):
        qs = ProfileModel.objects.all().order_by('user__username')
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(user__username__icontains=query) |
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query)
            )
        return qs


class ProfileUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = ProfileModel.objects.all()
    lookup_field = 'user__username'


class ProfileDetailAPIView(generics.RetrieveAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = ProfileSerializer
    parser_classes = (FileUploadParser,)
    queryset = ProfileModel.objects.all()
    lookup_field = 'user__username'
    permission_classes = [MyUserPermissions]
  # parser_classes = [FileUploadParser]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)


class ProfilePictureDetailAPIView(generics.RetrieveAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = ProfilePictureSerializer
    queryset = ProfileModel.objects.all()
    lookup_field = 'user__username'
    permission_classes = [MyUserPermissions]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)

# SKILLS


class SkillListAPIView(generics.ListAPIView):
    serializer_class = SkillSerializer
    queryset = SkillModel.objects.all().order_by('name')
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SkillFilter
    pagination_class = pagination.StandardResultsPagination


class SkillCreateAPIView(generics.CreateAPIView):
    serializer_class = SkillSerializer
    queryset = SkillModel.objects.all()
    permission_classes = [permissions.IsAdminUser]


class SkillDetailAPIView(generics.RetrieveAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = SkillSerializer
    queryset = SkillModel.objects.all()
    permission_classes = [MyAdminPermission]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)

# LINKS


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
# PORTFOLIOS


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


# LEVELS

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

# CERTIFICATIONS


class CertificationCreateAPIView(generics.CreateAPIView):
    serializer_class = CertificationSerializer
    queryset = CertificationModel.objects.all()
    permissions_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer, *args, **kwargs):
        serializer.save(user=self.request.user)


class CertificationDetailAPIView(generics.RetrieveAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = CertificationSerializer
    queryset = CertificationModel.objects.all()
    permission_classes = [MyUserPermissions]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)


class UserCertificationListAPIView(generics.ListAPIView):
    serializer_class = CertificationSerializer
    pagination_class = pagination.StandardResultsPagination

    def get_queryset(self):
        username = self.kwargs['user__username']
        user = User.objects.get(username=username)
        qs = CertificationModel.objects.filter(user=user)
        return qs

# EDUCATION


class MajorCreateAPIView(generics.CreateAPIView):
    queryset = MajorModel.objects.all()
    serializer_class = MajorSerializer
    permission_classes = [permissions.IsAdminUser]


class MajorListAPIView(generics.ListAPIView):
    queryset = MajorModel.objects.all().order_by('name')
    serializer_class = MajorSerializer
    pagination_class = pagination.StandardResultsPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MajorFilter
    #     filter_backends = (filters.SearchFilter,)
    # search_fields = ('name',)

    # def get_queryset(self, *args, **kwargs):
    #     qs = MajorModel.objects.all().order_by('name')
    #     query = self.request.GET.get("major", None)
    #     if query is not None:
    #         qs = qs.filter(
    #             Q(name__icontains=query)
    #         )
    #     return qs


class SchoolCreateAPIView(generics.CreateAPIView):
    serializer_class = SchoolSerializer
    queryset = SchoolModel.objects.all()
    permission_classes = [permissions.IsAdminUser]


class SchoolListAPIView(generics.ListAPIView):
    serializer_class = SchoolSerializer
    queryset = SchoolModel.objects.all()
    pagination_class = pagination.StandardResultsPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SchoolFilter


class EducationCreateAPIView(generics.CreateAPIView):
    queryset = EducationModel.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer, *args, **kwargs):
        name = serializer.validated_data['school']
        school = SchoolModel.objects.get(name__iexact=name)
        name = serializer.validated_data['major']
        major = MajorModel.objects.get(name__iexact=name)
        serializer.save(user=self.request.user, school=school, major=major)


class UserEducationListAPIView(generics.ListAPIView):
    serializer_class = EducationSerializer
    pagination_class = pagination.StandardResultsPagination

    def get_queryset(self):
        username = self.kwargs['user__username']
        user = User.objects.get(username=username)
        qs = EducationModel.objects.filter(user=user)
        return qs


class EducationDetailAPIView(generics.RetrieveAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = EducationSerializer

    queryset = EducationModel.objects.all()

    permission_classes = [MyUserPermissions]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)














