from django.contrib import admin
from services.models import ServiceModel, CategoryModel
# Register your models here.
admin.site.register(ServiceModel)
admin.site.register(CategoryModel)