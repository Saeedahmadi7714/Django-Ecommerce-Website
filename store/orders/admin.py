from django.contrib import admin

from orders.models import Discount


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    pass
