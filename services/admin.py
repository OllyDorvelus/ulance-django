from django.contrib import admin
from services.models import ServiceModel, CategoryModel, ServicePictureModel, JobModel
# Register your models here.


class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'price', 'purchases']


class JobModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class ServicePictureModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'description']


admin.site.register(ServiceModel, ServiceModelAdmin)
admin.site.register(JobModel, JobModelAdmin)
admin.site.register(CategoryModel, CategoryModelAdmin)
admin.site.register(ServicePictureModel, ServicePictureModelAdmin)
