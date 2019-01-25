from django.urls import path
from . import views

app_name = 'accounts_api'

urlpatterns = [
    path('', views.UserModelListAPIView.as_view(), name='accounts-api'),
    path('register/', views.UserCreateAPIView.as_view(), name='accounts-register-api'),
    path('login/', views.UserLoginAPIView.as_view(), name='accounts-login-api'),
]