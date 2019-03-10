# from django.shortcuts import render
# from django.forms import model_to_dict
# from django.http import JsonResponse
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.contrib.auth import authenticate, login, logout
from django.views.generic import DetailView, ListView, TemplateView
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
# from profiles.models import ProfileModel, SkillModel, LevelModel, CertificationModel, EducationModel, LinkModel
from services.models import ServiceModel, CategoryModel
from django.contrib.auth.mixins import LoginRequiredMixin

User = get_user_model()

# Create your views here.


class ServiceDetailView(DetailView):
    template_name = 'service_detail.html'
    queryset = ServiceModel.objects.all()
    context_object_name = 'Service'

    def get_object(self):
        service = get_object_or_404(ServiceModel, pk=self.kwargs.get("pk"))
        return service


class ServiceCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'create_service.html'
    login_url = '/login/'


class JobCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'create_job.html'
    login_url = '/login/'


class ServiceCategoryListView(DetailView):
    template_name = 'service_category_list.html'
    queryset = CategoryModel.objects.all()
    context_object_name = 'category'

    def get_object(self):
        category = get_object_or_404(CategoryModel, name__iexact=self.kwargs.get('name'))
        return category
