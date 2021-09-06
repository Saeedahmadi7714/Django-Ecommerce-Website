from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

from conf import settings


class Customer(AbstractUser):
    first_name = models.CharField(_('first name'), max_length=150, help_text=_(
        'Required. 150 characters or fewer. Letters only.'), error_messages={
        'required': _("The first_name must be set."),
    }, )

    last_name = models.CharField(_('last name'), max_length=150, help_text=_(
        'Required. 150 characters or fewer. Letters only.'), error_messages={
        'required': _("The last_name must be set."),
    }, )
    phone_number_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$", message=_('Must enter a valid phone number'))
    phone_number = models.CharField(validators=[phone_number_regex], max_length=16, unique=True)
    avatar = models.ImageField(upload_to='customers_image', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = UserManager()

    class Meta:
        verbose_name = _('CustomUser')
        verbose_name_plural = _('CustomUsers')


class ShippingAddress(models.Model):
    # Users can have one or many addresses
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address1 = models.CharField(
        _("Address Line 1"),
        max_length=1024,
    )

    address2 = models.CharField(
        _("Address Line 1"),
        null=True,
        blank=True,
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

    class Meta:
        verbose_name = "Shipping Address"
        verbose_name_plural = "Shipping Addresses"
