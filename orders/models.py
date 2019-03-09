from django.db import models
from services.models import ServiceModel
from django.contrib.auth import settings
from ulance.models import OrderModel
import uuid
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.utils.datetime_safe import datetime
from django.core.exceptions import ValidationError
from simple_history.models import HistoricalRecords
# Create your models here.


class ServiceOrderModel(OrderModel):
    history = HistoricalRecords()

    def get_total(self):
        cost = 0
        for entry in self.order_entries.all():
            cost = cost + (entry.quantity * entry.service.price.amount)
        return cost

    def change_status(self, status):
        self.status = status
        self.save()

    def __str__(self):
        return f'{self.buyer.username} - {self.paid}'


@receiver(post_save, sender=ServiceOrderModel)
def new_order(sender, instance, **kwargs):
    pass


class CartModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart')
    item_count = models.PositiveIntegerField(default=0)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.item_count}'

    def get_total(self):
        cost = 0
        for entry in self.cart_entries.filter(is_ordered=False):
            cost = cost + (entry.quantity * entry.service.price.amount)
        return cost

    def get_count(self):
        count = 0
        for entry in self.cart_entries.filter(is_ordered=False):
            count += entry.quantity
        return count

    def remove_all_entries(self):
        self.cart_entries.all().delete()
        self.save()

    def clear_cart(self):
        self.cart_entries.clear()
        self.item_count = self.get_count()
        self.total = self.get_total()
        self.save()


class EntryModel(models.Model):
    STATUS_CHOICES = (
        ('ORD', 'Ordered'),
        ('INP', 'In Progress'),
        ('INC', 'Incomplete'),
        ('REF', 'Refunded'),
        ('COM', 'Complete'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    service = models.ForeignKey(ServiceModel, null=True, on_delete=models.CASCADE, related_name='service_entries')
    order = models.ForeignKey(ServiceOrderModel, null=True, blank=True, on_delete=models.CASCADE, related_name='order_entries')
    cart = models.ForeignKey(CartModel, null=True, blank=True, on_delete=models.CASCADE, related_name='cart_entries')
    quantity = models.PositiveIntegerField(default=1)
    buyer_notes = models.TextField(null=True, blank=True, max_length=1000)
    seller_notes = models.TextField(null=True, blank=True, max_length=1000)
    days_remaining = models.PositiveIntegerField(null=True, blank=True)
    is_ordered = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self, *args, **kwargs):
        if self.cart:
            if self.cart.cart_entries.filter(service=self.service):
                raise ValidationError("Service already in cart")
        if self.order and self.cart:
            raise ValidationError("Can't be part of an order and be in a cart")
        if self.status and not self.is_ordered:
            raise ValidationError("Can't have a status if it is not ordered")

    def __str__(self):
        if self.order:
            name = self.order.buyer.username
        elif self.cart:
            name = self.cart.user.username
        else:
            name = "no user"
        return f'{self.service.user.username} | {self.service.name} requested by {name}'


@receiver(pre_save, sender=EntryModel)
def remove_quantity(sender, instance, **kwargs):
    pass


@receiver(post_save, sender=EntryModel)
def update_cart(sender, instance, **kwargs):
    if instance.cart:
        cart = instance.cart
        cart.total = cart.get_total()
        cart.item_count = cart.get_count()
        cart.updated_at = datetime.now()
        cart.save()
        if instance.quantity <= 0:
           # cart.entries.delete(instance)
           instance.delete()


@receiver(post_delete, sender=EntryModel)
def remove_from_cart(sender, instance, **kwargs):
    if instance.cart:
        cart = instance.cart
        cart.total = cart.get_total()
        cart.item_count = cart.get_count()
        cart.updated_at = datetime.now()
        cart.save()


class ComplaintModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    reason = models.TextField(null=False, blank=False, max_length=1000)
    entry = models.OneToOneField(EntryModel, blank=False, null=False, on_delete=models.CASCADE, related_name='entry')
    is_valid_complaint = models.BooleanField(default=True)

    def clean(self, *args, **kwargs):
        if self.entry.status != 'COM':
            raise ValidationError("Entry need to be marked as completed before filing a complaint.")

    def __str__(self):
        return f'{self.entry.order.buyer.username} - {self.reason}'




