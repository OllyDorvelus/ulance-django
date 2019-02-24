from django.urls import path
from . import views

app_name = 'orders_api'

urlpatterns = [
     path('', views.OrderListAPIView.as_view(), name='order-list-api'),
     path('new/', views.OrderCreateAPIView.as_view(), name='order-create-api'),
     path('request/', views.ServiceOrderListAPIView.as_view(), name='request-list-api'),
     path('cart/', views.CartDetailAPIView.as_view(), name='cart-detail-api'),
     path('complaints/create/<entry_id>/', views.ComplaintCreateAPIView.as_view(), name='complaint-create-api'),
     path('complaints/<pk>', views.ComplaintDetailAPIView.as_view(), name='complaint-detail-api'),
     path('entries/<pk>/', views.EntryDetailAPIView.as_view(), name='entry-detail-api'),
     path('entries/service/<pk>/', views.ServiceOwnerEntryDetailAPIView.as_view(), name='entry-service-owner-detail-api'),
     path('entries/add/<service_id>/', views.AddEntryToCartAPIView.as_view(), name='add-entry-to-cart-api')
]
