from django.contrib import admin

from .models import (Customer, )


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    readonly_fields = ['username', 'phone_number', 'email']
    exclude = ['password', ]
