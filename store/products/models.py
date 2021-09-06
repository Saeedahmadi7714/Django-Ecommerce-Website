from django.db import models
from djmoney.models.fields import MoneyField
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('product_by_category', kwargs={'slug': self.slug})


class Product(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images')
    number_of_product = models.PositiveSmallIntegerField(blank=True, null=True)
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        ordering = ['-created']

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})
