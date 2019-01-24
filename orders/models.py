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
    service = models.ManyToManyField(ServiceModel, related_name='services')

    def is_empty_cart(self):
        return self.item_count == 0

    def add_to_cart(self):
        self.item_count += 1

    def reset_cart(self):
        self.item_count = 0

    def remove_from_cart(self):
        self.item_count -= 1

    def __str__(self):
        return self.user.username + " - " + self.item_count

class ServiceOrderModel(OrderModel):
    service = models.ManyToManyField(ServiceModel, blank=False, related_name='buyers')

