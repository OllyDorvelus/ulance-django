from django.contrib import admin
from services.models import ServiceModel, CategoryModel, ServicePictureModel
# Register your models here.


class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'price', 'purchases']


class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class ServicePictureModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'description']


admin.site.register(ServiceModel, ServiceModelAdmin)
admin.site.register(CategoryModel, CategoryModelAdmin)
admin.site.register(ServicePictureModel, ServicePictureModelAdmin)
