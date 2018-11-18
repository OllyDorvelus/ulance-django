from django.db import models
from profiles.models import ProfileModel
from django.conf import settings
from django.urls import reverse, reverse_lazy
from djmoney.models.fields import MoneyField
from . import validators
import uuid
from ulance.models import PictureModel
# Create your models here.
from django.db.models import Count, Avg, Value, Sum



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

class ServiceManager(models.Manager):
    def get_queryset(self):
        return super(ServiceManager, self).get_queryset().annotate(avg_rate=Avg('reviews__rate'), purchases=Count('buyers'))


class ServiceModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owner')
    name = models.CharField(max_length=100, blank=False, null=False)
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    category = models.ManyToManyField(CategoryModel, related_name='categories', blank=True)
    description = models.TextField(blank=False, null=False, max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ServiceManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('services:service-detail', kwargs={'pk': self.pk})

class ServicePictureModel(PictureModel):
    service = models.ForeignKey(ServiceModel, null=False, on_delete=models.CASCADE, blank=False, related_name='photos')

class TransactionModel(models.Model):
    STATUS_CHOICES = (
        ('ORD', 'Ordered'),
        ('INP', 'In Progress'),
        ('INC', 'Incomplete'),
        ('REF', 'Refunded'),
        ('COM', 'Complete'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=False)
    paid = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    status = models.CharField(max_length=3, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class ServiceTransactionModel(TransactionModel):
    service = models.ForeignKey(ServiceModel, on_delete=models.SET_NULL, null=True, blank=False, related_name='buyers')


class ReviewModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviewer')
    description = models.TextField(blank=True, max_length=300)
    rate = models.IntegerField(validators=[validators.validate_rate])
    service = models.ForeignKey(ServiceModel, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.user.username + ' - ' + str(self.rate)




