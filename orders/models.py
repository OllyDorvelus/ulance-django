from django.db import models
from services.models import ServiceModel
from django.contrib.auth import settings
from ulance.models import OrderModel
import uuid
# Create your models here.


class CartModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owner')
    item_count = models.PositiveIntegerField(default=0)
    # service = models.ManyToManyField(ServiceModel, related_name='services', blank=True)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # def is_cart_empty(self):
    #     return self.item_count == 0
    #
    # def add_to_cart(self):
    #     self.item_count += 1
    #
    # def reset_cart(self):
    #     self.item_count = 0
    #
    # def remove_from_cart(self):
    #     self.item_count -= 1
    # @property
    # def items(self):
    #     return self.service.count()
    #
    # def clear(self):
    #     self.service.clear()
    #
    # def remove(self, service):
    #     if service in self.service.all():
    #         self.service.remove(service)
    #     else:
    #         return "Cannot remove service"

    def __str__(self):
        return f'{self.user.username} - {self.item_count}'


class EntryModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    service = models.ForeignKey(ServiceModel, null=True, on_delete=models.CASCADE, related_name='services')
    cart = models.ForeignKey(CartModel, null=True, on_delete=models.CASCADE, related_name='entries')
    quantity = models.PositiveIntegerField(default=1)


class ServiceOrderModel(OrderModel):
    service = models.ManyToManyField(ServiceModel, blank=False, related_name='buyers')

