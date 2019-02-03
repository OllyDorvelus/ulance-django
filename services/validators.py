from django.core.exceptions import ValidationError


def validate_rate(value):
    if value > 10 or value < 0:
        raise ValidationError(u'Please pick a number between 0 and 10, inclusive')
