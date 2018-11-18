from django.contrib import admin
from services.models import ServiceModel, CategoryModel, ReviewModel, ServiceTransactionModel
# Register your models here.

class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'price']

class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'description', 'rate', 'service']

class ServiceTransactionModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'service', 'paid', 'buyer', 'status']


admin.site.register(ServiceModel, ServiceModelAdmin)
admin.site.register(CategoryModel, CategoryModelAdmin)
admin.site.register(ReviewModel, ReviewModelAdmin)
admin.site.register(ServiceTransactionModel, ServiceTransactionModelAdmin)