from django.urls import path
from . import views

app_name = 'orders_api'

urlpatterns = [
     path('', views.OrderListAPIView.as_view(), name='order-list-api'),
     path('new/<service_id>/service/', views.ServiceOrderCreateAPIView.as_view(), name='service-order-create-api'),
     path('new/<job_id>/job/', views.JobOrderCreateAPIView.as_view(), name='job-order-create-view'),
     path('manage/', views.ServiceOrderListAPIView.as_view(), name='request-list-api'),
     path('complete/', views.ServiceOrderCompleteListAPIView.as_view(), name='complete-order-list-api'),
   #  path('cart/', views.CartDetailAPIView.as_view(), name='cart-detail-api'),
   #  path('complaints/create/<entry_id>/', views.ComplaintCreateAPIView.as_view(), name='complaint-create-api'),
   #  path('complaints/<pk>', views.ComplaintDetailAPIView.as_view(), name='complaint-detail-api'),
   #  path('entries/<pk>/', views.EntryDetailAPIView.as_view(), name='entry-detail-api'),
   #  path('entries/service/<pk>/', views.ServiceOwnerEntryDetailAPIView.as_view(),
   #       name='entry-service-owner-detail-api'),
   #  path('entries/add/<service_id>/', views.AddEntryToCartAPIView.as_view(), name='add-entry-to-cart-api')
]
