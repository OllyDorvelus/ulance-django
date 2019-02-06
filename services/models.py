from django.db import models
from django.conf import settings
from django.urls import reverse, reverse_lazy
from djmoney.models.fields import MoneyField
from . import validators
import uuid
from ulance.models import PictureModel
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.utils.datetime_safe import datetime
from django.db.models import Count, Avg, Value, Sum
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

    @property
    def get_name(self):
        return self.name

    def get_all_sub_categories(self):
        if self.parent:
            return self.children.all()
        return []

# class ServiceManager(models.Manager):
#     def get_queryset(self):
#         return super(ServiceManager, self).get_queryset().annotate(avg_rate_sort=Avg('reviews__rate'), purchases_sort=Count('service_entries'))


class ServiceModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='services')
    name = models.CharField(max_length=100, blank=False, null=False)
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    category = models.ManyToManyField(CategoryModel, related_name='categories', blank=True)
    description = models.TextField(blank=False, null=False, max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    purchases = models.PositiveIntegerField(default=0)
    average_rating = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=4)
    # objects = ServiceManager()

    def get_avg_rating(self):
        if self.reviews.count():
            total = 0
            count = 0
            for review in self.reviews.all():
                total += review.rate
                count += 1
            avg = total / count
            return round(avg, 2)
        return 0

    def get_purchases(self):
        total = 0
        for entry in self.service_entries.filter(is_ordered=True):
            total += entry.quantity
        return total

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('services:service-detail', kwargs={'pk': self.pk})


class ServicePictureModel(PictureModel):
    service = models.ForeignKey(ServiceModel, null=False, on_delete=models.CASCADE, blank=False, related_name='service_photos')


class ReviewModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviewer')
    description = models.TextField(blank=False, null=False, max_length=300)
    rate = models.IntegerField(validators=[validators.validate_rate])
    service = models.ForeignKey(ServiceModel, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.user.username + ' - ' + str(self.rate)

    def clean(self, *args, **kwargs):
        if self.service.reviews.filter(user=self.user):
            raise ValidationError("You already wrote an review")


@receiver(post_save, sender=ReviewModel)
def update_avg_rating_add_or_update(sender, instance, **kwargs):
    service = instance.service
    service.average_rating = service.get_avg_rating()
    service.save()


@receiver(post_delete, sender=ReviewModel)
def update_avg_rating_delete(sender, instance, **kwargs):
    service = instance.service
    service.average_rating = service.get_avg_rating()
    service.save()




