__author__ = '13477'
from django.urls import path
from . import views

app_name = 'servicesapi'

urlpatterns = [
    path('', views.ServiceListAPIView.as_view(), name='service-list-api'),
    path('categories/', views.CategoryListAPIView.as_view(), name='category-list-api'),
    path('categories/create/', views.CategoryCreateAPIView.as_view(), name='category-create-api'),
    path('categories/<pk>/', views.CategoryDetailAPIView.as_view(), name='category-detail-api'),
    path('create/', views.ServiceCreateAPIView.as_view(), name='service-create-api'),
    path('<pk>/', views.ServiceDetailAPIView.as_view(), name='service-detail-api'),
    path('<user__username>/services/', views.UserServiceListAPIView.as_view(), name='user-service-list-api'),
    path('<user__username>/services/', views.UserServiceListAPIView.as_view(), name='user-service-list-api'),


]