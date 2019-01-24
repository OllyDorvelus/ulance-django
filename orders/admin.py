from django.contrib import admin
from .models import CartModel, ServiceOrderModel
# Register your models here.

# class CartModelAdmin(admin.ModelAdmin):
#     list_display = []
#
# class ServiceOrderModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'service', 'paid', 'buyer', 'status']