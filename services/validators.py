from django.core.exceptions import ValidationError


def validate_rate(value):
    if value > 10 or value < 0:
        raise ValidationError(u'Please pick a number between 0 and 10, inclusive')


# def validate_five_pictures_per_service(obj):
#     model = obj.__class__
#     if (model.service_photos.count() > 1 and
#             obj.pk != model.service_photos.get().pk):
#         raise ValidationError("Can only create 1 %s instance" % model.__name__)
