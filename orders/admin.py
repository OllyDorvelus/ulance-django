from django.contrib import admin
from .models import CartModel, ServiceOrderModel, EntryModel, ComplaintModel
# Register your models here.


class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'item_count', 'total']


class ServiceOrderModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'paid', 'buyer', 'status']


class EntryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'cart', 'service', 'quantity']


class ComplaintModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'entry', 'reason', 'is_valid_complaint']


admin.site.register(CartModel, CartModelAdmin)
admin.site.register(ServiceOrderModel, ServiceOrderModelAdmin)
admin.site.register(EntryModel, EntryModelAdmin)
admin.site.register(ComplaintModel, ComplaintModelAdmin)