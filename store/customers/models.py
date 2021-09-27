from django.db import (models)
from django.contrib.auth.models import (AbstractUser)
from django.utils.translation import gettext_lazy as _
from django.core.validators import (RegexValidator)

from conf import settings


class Customer(AbstractUser):
    phone_number_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$", message=_('Must enter a valid phone number'))
    phone_number = models.CharField(validators=[phone_number_regex], max_length=16, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = _("customers")
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')

    def __str__(self):
        return f'{self.first_name}{self.last_name}'


class Address(models.Model):
    HOME = 'home'
    OFFICE = 'office'
    ADDRESS_TYPE = [
        (HOME, _('home')),
        (OFFICE, _('office')),
    ]

    # Users can have one or many addresses
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(
        _("Address"),
        max_length=1024,
    )

    country = models.CharField(
        _("Country"),
        max_length=3,
    )

    state = models.CharField(
        _("State"),
        max_length=150,
    )

    city = models.CharField(
        _("City"),
        max_length=150,
    )

    postcode = models.CharField(
        _("Postcode"),
        max_length=12,
    )
    address_type = models.CharField(
        max_length=6,
        choices=ADDRESS_TYPE,
        default=HOME
    )
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        db_table = _("addresses")
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")

    def __str__(self):
        return f'{self.address}'
