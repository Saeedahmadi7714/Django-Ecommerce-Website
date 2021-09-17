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


class Address(models.Model):
    # Users can have one or many addresses
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(
        _("Address Line "),
        max_length=1024,
    )

    postcode = models.CharField(
        _("Postcode"),
        max_length=12,
    )

    city = models.CharField(
        _("City"),
        max_length=1024,
    )

    country = models.CharField(
        _("Country"),
        max_length=3,
    )
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    is_default = models.BooleanField(default=False)

    class Meta:
        db_table = _("addresses")
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")
