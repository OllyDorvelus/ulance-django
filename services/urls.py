from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('services/new/', views.ServiceCreateView.as_view(), name='service-create'),
    path('services/<pk>/', views.ServiceDetailView.as_view(), name='service-detail'),
    path('services/categories/<name>/', views.ServiceCategoryListView.as_view(), name='service-category-list')
]