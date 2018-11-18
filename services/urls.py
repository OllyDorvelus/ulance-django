from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('services/<pk>/', views.ServiceDetailView.as_view(), name='service-detail')
]