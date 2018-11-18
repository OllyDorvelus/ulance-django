from django.shortcuts import render
from django.forms import model_to_dict
from django.http import JsonResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View, DetailView, ListView, FormView
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from profiles.models import ProfileModel, SkillModel, LevelModel, CertificationModel, EducationModel, LinkModel

User = get_user_model()

# Create your views here.

class UserDetailView(DetailView):
   # template_name = 'profile_detail.html'
    queryset = User.objects.all()
    context_object_name = 'User'

    def get_object(self):
        user = get_object_or_404(User, username__iexact=self.kwargs.get("username"))
        return user

    # def get_context_data(self, *args, **kwargs):
    #     context = super(UserDetailView, self).get_context_data(*args, **kwargs)
    #     user = UserDetailView.get_object(self)
    #     Levels = LevelModel.objects.filter(user=user)
    #     Certifications = CertificationModel.objects.filter(user=user)
    #     Educations = EducationModel.objects.filter(user=user)
    #     Links = LinkModel.objects.filter(user=user)
    #     context['Levels'] = Levels
    #     context['Certifications'] = Certifications
    #     context['Educations'] = Educations
    #     context['Links'] = Links
    #     return context

    def get_template_names(self, *args, **kwargs):
        user = User.objects.get(username__iexact=UserDetailView.get_object(self).username)
        if self.request.user == user:
            return 'profile_detail_edit.html'
        else:
            return 'profile_detail_edit.html'