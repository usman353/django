from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )


CATEGORIES = ['Paki', 'Seafood','Desi','Chinese']


def validate_categories(value):
    if not value.title() in CATEGORIES:
        raise ValidationError(f'{value} not a valid category.')
