from django.contrib import admin
from services.models import ServiceModel, CategoryModel
# Register your models here.

class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name']

class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(ServiceModel, ServiceModelAdmin)
admin.site.register(CategoryModel, CategoryModelAdmin)