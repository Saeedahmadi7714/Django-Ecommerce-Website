from django.db import models
from djmoney.models.fields import MoneyField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class IPaddress(models.Model):
    ip_address = models.GenericIPAddressField()

    class Meta:
        db_table = _('ip_addresses')
        verbose_name = _('ip_address')
        verbose_name_plural = _('IPaddress')

    def __str__(self):
        return f'{self.ip_address}'


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = _('categories')
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField()
    image = models.ImageField(upload_to='product_images')
    number_of_product = models.PositiveSmallIntegerField(blank=True, null=True)
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    views = models.ManyToManyField(IPaddress, blank=True)

    class Meta:
        db_table = _('products')
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        ordering = ['-created']

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})


class Contact(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(max_length=150, null=True, blank=True)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = _('contacts')
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')

    def __str__(self):
        return f'{self.name}'
