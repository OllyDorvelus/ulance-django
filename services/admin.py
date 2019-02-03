from django.contrib import admin
from services.models import ServiceModel, CategoryModel, ReviewModel, ServicePictureModel
# Register your models here.


class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'price', 'average_rating', 'purchases']


class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'description', 'rate', 'service']


class ServicePictureModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'description']


admin.site.register(ServiceModel, ServiceModelAdmin)
admin.site.register(CategoryModel, CategoryModelAdmin)
admin.site.register(ReviewModel, ReviewModelAdmin)
admin.site.register(ServicePictureModel, ServicePictureModelAdmin)
