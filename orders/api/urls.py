from django.urls import path
from . import views

app_name = 'orders_api'

urlpatterns = [
     path('', views.OrderListAPIView.as_view(), name='order-list-api'),
     path('cart/', views.CartDetailAPIView.as_view(), name='cart-detail-api'),
    # path('new/', views.CreateOrderAPIView.as_view(), name='order-create-api'),
    # path('<pk>/', views.OrderDetailAPIView.as_view(), name='order-detail-api'),
    # path('entries/', views.EntryListAPIView.as_view(), name='entry-list-api'),
    path('entry/<pk>/', views.EntryDetailAPIView.as_view(), name='entry-detail-view'),
    path('entry/add/<pk>', views.AddEntryToCartAPIView.as_view(), name='add-entry-to-cart-api')
   # path('entry/remove/<pk>', views.RemoveEntryFromCartAPIView.as_view(), name='remove-entry-form-cart-api'),

]