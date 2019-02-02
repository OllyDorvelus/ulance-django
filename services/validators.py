from django.core.exceptions import ValidationError


def validate_rate(value):
    if value > 5 or value < 0:
        raise ValidationError(u'Please pick a number between 0 and 5, inclusive')
