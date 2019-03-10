from django.db import models
from django.conf import settings
from django.urls import reverse, reverse_lazy
from djmoney.models.fields import MoneyField
import uuid
from ulance.models import PictureModel
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.utils.datetime_safe import datetime
from django.db.models import Count, Avg, Value, Sum
from decimal import DecimalException
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
            return f'{self.parent.name} - {self.name}'
        else:
            return self.name

    @property
    def get_name(self):
        return self.name

    def get_all_sub_categories(self):
        if self.is_parent:
            return self.children.all()
        return []

# class ServiceManager(models.Manager):
#     def get_queryset(self):
#         return super(ServiceManager, self).get_queryset().annotate(avg_rate_sort=Avg('reviews__rate'), purchases_sort=Count('service_entries'))


class ServiceModel(models.Model):
    DELIVERY_CHOICES = (
        ('Early', '1-3'),
        ('Normal', '3-5'),
        ('Later', '7+')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='services')
    name = models.CharField(max_length=100, blank=False, null=False)
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    category = models.ManyToManyField(CategoryModel, related_name='service', blank=True)
    description = models.TextField(blank=False, null=False, max_length=500)
    delivery_time = models.CharField(max_length=20, choices=DELIVERY_CHOICES, blank=False, null=False, default='Normal')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    purchases = models.PositiveIntegerField(default=0)
    portfolio_link = models.URLField(null=True, blank=True)
  #  average_rating = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=4)
    # objects = ServiceManager()

    # def get_avg_rating(self):
    #     if self.reviews.count():
    #         total = 0
    #         count = 0
    #         for review in self.reviews.all():
    #             total += review.rate
    #             count += 1
    #         avg = total / count
    #         return round(avg, 2)
    #     return 0.00

    # def get_purchases(self):
    #     total = 0
    #     for entry in self.service_entries.filter(is_ordered=True):
    #         total += entry.quantity
    #     return total

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('services:service-detail', kwargs={'pk': self.pk})


class ServicePictureModel(PictureModel):
    service = models.ForeignKey(ServiceModel, null=False, on_delete=models.CASCADE, blank=False, related_name='photos')


class JobModel(models.Model):
    STATUS_CHOICES = (
        ('NT', 'Not Taken'),
        ('T', 'Taken'),
        ('COM', 'Completed'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    freelancer = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=75, blank=False, null=False)
    category = models.ManyToManyField(CategoryModel, related_name='job', blank=True)
    description = models.TextField(max_length=10000, blank=False, null=False)
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    status = models.CharField(choices=STATUS_CHOICES, default='NT', max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)







