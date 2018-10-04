from django.db import models
from profiles.models import ProfileModel
from django.conf import settings
from django.urls import reverse, reverse_lazy
import uuid
# Create your models here.


class CategoryModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, blank=False, null=False)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    is_parent = models.BooleanField(verbose_name='is a parent category', default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.parent:
            return self.parent.name + " - " + self.name
        else:
            return self.name

class ServiceModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owner')
    name = models.CharField(max_length=100, blank=False, null=False)
    category = models.ManyToManyField(CategoryModel, related_name='categories')
    buyer = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='buyers')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name




