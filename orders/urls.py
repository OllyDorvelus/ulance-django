from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('cart/', views.CartDetailView.as_view(), name='cart-detail-view'),
    path('order/history/', views.OrderHistoryView.as_view(), name='order-history-view'),
    path('orders/manage/', views.ManageOrdersView.as_view(), name='manage-orders-view')
]