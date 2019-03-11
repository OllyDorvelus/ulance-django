from rest_framework import generics, permissions, mixins
from .serializers import ( ServiceSerializer, CategorySerializer, ServiceCreateSerializer, JobSerializer, JobCreateSerializer )
from profiles.api.serializers import SkillSerializer
from services.models import ServiceModel, CategoryModel, JobModel
from profiles.models import SkillModel
from ulance import pagination
from ulance.custom_permissions import MyUserPermissions, MyAdminPermission, StrictUserPermissions
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ServiceFilter
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

User = get_user_model()

# SERVICES


class ServiceListAPIView(generics.ListAPIView):
    serializer_class = ServiceSerializer
    queryset = ServiceModel.objects.all().order_by('name')
    pagination_class = pagination.StandardResultsPagination
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ("price", "average_rating", "purchases")
    filterset_class = ServiceFilter


class ServiceCreateAPIView(generics.CreateAPIView):
    serializer_class = ServiceCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer, *args, **kwargs):
        serializer.save(user=self.request.user)


class ServiceDetailAPIView(generics.RetrieveAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = ServiceSerializer
    queryset = ServiceModel.objects.all()
    permission_classes = [MyUserPermissions]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)


class UserServiceListAPIView(generics.ListAPIView):
    serializer_class = ServiceSerializer
    pagination_class = pagination.StandardResultsPagination

    def get_queryset(self, *args, **kwargs):
        username = self.kwargs['user__username']
        user = User.objects.get(username=username)
        qs = ServiceModel.objects.filter(user=user)
        return qs


class CategoryServiceListAPIView(generics.ListAPIView):
    serializer_class = ServiceSerializer
    pagination_class = pagination.StandardResultsPagination
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ("price", "average_rating", "purchases")
    filterset_class = ServiceFilter

    def get_queryset(self, *args, **kwargs):
        category_name = self.kwargs['category_name']
        category = get_object_or_404(CategoryModel, name__iexact=category_name)
        qs = ServiceModel.objects.filter(category=category).order_by('name')
        return qs


class ServiceReviewListAPIView(generics.ListAPIView):
    pass
    # serializer_class = ReviewSerializer
    # pagination_class = pagination.StandardResultsPagination
    #
    # def get_queryset(self, *args, **kwargs):
    #     pk = self.kwargs['pk']
    #     service = ServiceModel.objects.get(pk=pk)
    #     qs = ReviewModel.objects.filter(service=service).order_by('updated_at')
    #     return qs


class RemoveCategoryAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        category_pk = self.kwargs['category_pk']
        service_pk = self.kwargs['service_pk']

        category = CategoryModel.objects.filter(pk=category_pk).first()#get_object_or_404(CategoryModel, category_pk)
        service = ServiceModel.objects.filter(pk=service_pk).first()#get_object_or_404(ServiceModel, service_pk)
        if category is None or service is None:
            return Response({'message': 'Invalid category or service'}, status=404)
        if request.user != service.user or not request.user.is_superuser:
            return Response({'message': 'Not Authorized To Perform This Action'}, status=401)
        message = "Category is not listed in service"
        if service.categories.filter(pk=category.pk).exists():
            service.categories.remove(category)
            service.save()
            return Response({"message": "Category removed"}, status=201)
        return Response({'message': message}, status=400)


class AddCategoryAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        category_pk = self.kwargs['category_pk']
        service_pk = self.kwargs['service_pk']

        category = CategoryModel.objects.filter(pk=category_pk).first()
        service = ServiceModel.objects.filter(pk=service_pk).first()
        if category is None or service is None:
            return Response({'message': 'Invalid category or service'}, status=404)
        if request.user != service.user or not request.user.is_superuser:
            return Response({'message': 'Not Authorized To Perform This Action'}, status=401)
        message = "Service already has this category"
        if not service.categories.filter(pk=category.pk).exists():
            if service.categories.filter(is_parent=False).count() > 10:
                return Response({'message': 'Can not exceed more than 10 sub categories'}, status=400)
            if service.categories.filter(is_parent=True).count() > 3:
                return Response({'message': 'Can not exceed more than 3 main categories'}, status=400)
            service.categories.add(category)
            service.save()
            return Response({"message": "Category added"}, status=201)
        return Response({'message': message}, status=400)

# JOBS


class RemoveJobCategoryAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        category_pk = self.kwargs['category_pk']
        job_pk = self.kwargs['job_pk']

        category = CategoryModel.objects.filter(pk=category_pk).first()#get_object_or_404(CategoryModel, category_pk)
        job = JobModel.objects.filter(pk=job_pk).first()#get_object_or_404(ServiceModel, service_pk)
        if category is None or job is None:
            return Response({'message': 'Invalid category or job'}, status=404)
        if request.user != job.user or not request.user.is_superuser:
            return Response({'message': 'Not Authorized To Perform This Action'}, status=401)
        message = "Category is not listed in job"
        if job.categories.filter(pk=category.pk).exists():
            job.categories.remove(category)
            job.save()
            return Response({"message": "Category removed"}, status=201)
        return Response({'message': message}, status=400)


class AddJobCategoryAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        category_pk = self.kwargs['category_pk']
        job_pk = self.kwargs['job_pk']

        category = CategoryModel.objects.filter(pk=category_pk).first()
        job = JobModel.objects.filter(pk=job_pk).first()
        if category is None or job is None:
            return Response({'message': 'Invalid category or job'}, status=404)
        if request.user != job.user or not request.user.is_superuser:
            return Response({'message': 'Not Authorized To Perform This Action'}, status=401)
        message = "Job already has this category"
        if not job.categories.filter(pk=category.pk).exists():
            if job.categories.filter(is_parent=False).count() > 10:
                return Response({'message': 'Can not exceed more than 10 sub categories'}, status=400)
            if job.categories.filter(is_parent=True).count() > 3:
                return Response({'message': 'Can not exceed more than 3 main categories'}, status=400)
            job.categories.add(category)
            job.save()
            return Response({"message": "Category added"}, status=201)
        return Response({'message': message}, status=400)


class AddJobSkillAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        skill_pk = self.kwargs['skill_pk']
        job_pk = self.kwargs['job_pk']

        skill = SkillModel.objects.filter(pk=skill_pk).first()
        job = JobModel.objects.filter(pk=job_pk).first()
        if skill is None or job is None:
            return Response({'message': 'Invalid skill or job'}, status=404)
        if request.user != job.user or not request.user.is_superuser:
            return Response({'message': 'Not Authorized To Perform This Action'}, status=401)
        message = "Job already has this Skill"
        if not job.skill.filter(pk=skill.pk).exists():
            if job.skill.filter(is_parent=False).count() > 30:
                return Response({'message': 'Can not exceed more than 30 skills'}, status=400)
            job.skill.add(skill)
            job.save()
            return Response({"message": "Skill added"}, status=201)
        return Response({'message': message}, status=400)


class RemoveJobSkillAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        skill_pk = self.kwargs['skill_pk']
        job_pk = self.kwargs['job_pk']

        skill = SkillModel.objects.filter(pk=skill_pk).first()#get_object_or_404(CategoryModel, category_pk)
        job = JobModel.objects.filter(pk=job_pk).first()#get_object_or_404(ServiceModel, service_pk)
        if skill is None or job is None:
            return Response({'message': 'Invalid skill or job'}, status=404)
        if request.user != job.user or not request.user.is_superuser:
            return Response({'message': 'Not Authorized To Perform This Action'}, status=401)
        message = "Skill is not listed in job"
        if job.skill.filter(pk=skill.pk).exists():
            job.skill.remove(skill)
            job.save()
            return Response({"message": "Category removed"}, status=201)
        return Response({'message': message}, status=400)


class JobSkillListAPIView(generics.ListAPIView):
    serializer_class = SkillSerializer
    pagination_class = pagination.StandardResultsPagination

    def get_queryset(self):
        job_id = self.kwargs['job_id']
        job = get_object_or_404(JobModel, pk=job_id)
        job_skills = SkillModel.objects.filter(job=job).order_by("name")
        return job_skills


class JobListAPIView(generics.ListAPIView):
    serializer_class = JobSerializer
    queryset = JobModel.objects.all().order_by('created_at')
    pagination_class = pagination.StandardResultsPagination
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ("name",)
  #  filterset_class = JobFilter


class JobCreateAPIView(generics.CreateAPIView):
    serializer_class = JobCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class JobDetailAPIView(generics.RetrieveAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = JobSerializer
    queryset = JobModel.objects.all()
    permission_classes = [MyUserPermissions]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)

# CATEGORIES


class CategoryListAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = CategoryModel.objects.all().order_by('name')
    pagination_class = pagination.StandardResultsPagination


class MainCategoryListAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = CategoryModel.objects.filter(is_parent=True)
    pagination_class = pagination.StandardResultsPagination


class SubCategoryListAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer
    pagination_class = pagination.StandardResultsPagination

    def get_queryset(self, *args, **kwargs):
        category_parent_id = self.kwargs['pk']
        category = get_object_or_404(CategoryModel, pk=category_parent_id)
        sub_categories = category.children.all().order_by('name')
        return sub_categories


class ServiceCategoryListAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self, *args, **kwargs):
        service_id = self.kwargs['service_pk']
        service = get_object_or_404(ServiceModel, pk=service_id)
        service_categories = CategoryModel.objects.filter(service=service).order_by('name')
        return service_categories


class CategoryCreateAPIView(generics.CreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]


class CategoryDetailAPIView(generics.RetrieveAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = CategorySerializer
    queryset = CategoryModel.objects.all()
    permission_classes = [MyAdminPermission]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)

# REVIEWS


class ReviewCreateAPIView(generics.CreateAPIView):
        pass
#     serializer_class = ReviewSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = self.request.user
#         service_id = self.kwargs['pk']
#         service = ServiceModel.objects.get(pk=service_id)
#         if service.reviews.filter(user=user).exists():
#             return Response({"message": "You already wrote a review for this service"}, status=status.HTTP_400_BAD_REQUEST)
#         serializer.validated_data['service'] = service
#         serializer.validated_data['user'] = user
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
#
#     def perform_create(self, serializer, *args, **kwargs):
#         serializer.save()
#
#
class ReviewDetailAPIView(generics.RetrieveAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    pass
#     serializer_class = ReviewSerializer
#     queryset = ReviewModel.objects.all()
#     permission_classes = [MyUserPermissions]
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(self, request, *args, **kwargs)




