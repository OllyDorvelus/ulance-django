from django.contrib import admin
from .models import CartModel, ServiceOrderModel, EntryModel
# Register your models here.


class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']


class ServiceOrderModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'paid', 'buyer', 'status']


class EntryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'cart', 'service', 'quantity']


admin.site.register(CartModel, CartModelAdmin)
admin.site.register(ServiceOrderModel, ServiceOrderModelAdmin)
admin.site.register(EntryModel, EntryModelAdmin)