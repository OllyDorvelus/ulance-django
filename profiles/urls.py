from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('user/<username>/', views.UserDetailView.as_view(), name='profile-detail'),
]