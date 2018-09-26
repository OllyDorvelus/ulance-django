__author__ = '13477'

app_name = 'accountsapi'
from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserModelListAPIView.as_view(), name='accounts-list-api'),
    path('register/', views.UserCreateAPIView.as_view(), name='accounts-register-api'),
    path('login/', views.UserLoginAPIView.as_view(), name='accounts-login-api'),
]