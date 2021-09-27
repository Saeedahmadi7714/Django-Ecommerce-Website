from django.db import models
from django.utils.translation import gettext_lazy as _
from conf import settings
from customers.models import Address
from products.models import Product
from djmoney.models.fields import MoneyField


class Discount(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                                 related_name='discounts')
    amount = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    expire_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = _('discounts')
        verbose_name = _('Discount')
        verbose_name_plural = _('Discounts')

    def __str__(self):
        return f'{self.customer} {self.amount}%'


class OrderItem(models.Model):
    product = models.ManyToManyField(Product)
    quantity = models.SmallIntegerField()


class Order(models.Model):
    READY_TO_SHIP = 'ready_to_ship'
    SENDING = 'sending'
    SENT = 'sent'
    STATUS = [
        (READY_TO_SHIP, _('ready_to_ship')),
        (SENDING, _('sending')),
        (SENT, _('sent')),
    ]

    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='orders')
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    products = models.ManyToManyField(OrderItem, on_delete=models.RESTRICT)
    status = models.CharField(
        max_length=15,
        choices=STATUS,
        default=READY_TO_SHIP,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    total_price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    discount = models.OneToOneField(Discount, on_delete=models.RESTRICT)
    total_price_with_discount = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', blank=True,
                                           null=True)

    class Meta:
        db_table = _('orders')
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return f'{self.customer}'
