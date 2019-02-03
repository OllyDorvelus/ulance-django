from django.db import models
from django.conf import settings
import uuid
from djmoney.models.fields import MoneyField


class PictureModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    photo = models.ImageField(upload_to='pictures')
    description = models.TextField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class OrderModel(models.Model):
    STATUS_CHOICES = (
        ('ORD', 'Ordered'),
        ('INP', 'In Progress'),
        ('INC', 'Incomplete'),
        ('REF', 'Refunded'),
        ('COM', 'Complete'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    buyer = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    paid = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='INP')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

