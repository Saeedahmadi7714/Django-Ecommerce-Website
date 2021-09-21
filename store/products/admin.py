from django.contrib import admin

from products.models import (Category, Product, IPaddress)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(IPaddress)
class IpAddressAdmin(admin.ModelAdmin):
    pass
