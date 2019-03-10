from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('services/new/', views.ServiceCreateView.as_view(), name='service-create'),
    path('jobs/new', views.JobCreateView.as_view(), name='job-create'),
    path('services/<pk>/', views.ServiceDetailView.as_view(), name='service-detail'),
    path('services/categories/<name>/', views.ServiceCategoryListView.as_view(), name='category-service-list')
]