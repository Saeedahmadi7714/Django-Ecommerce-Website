from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Customer

UserAdmin.fieldsets[1][1]['fields'] = (
    'first_name',
    'last_name',
    'email',
    # Customer model's custom field
    'phone_number',
)

# Admin can not change user account information
UserAdmin.readonly_fields = (
    'username',
    'first_name',
    'last_name',
    'email',
    'phone_number',
    'last_login',
    'date_joined'
)

UserAdmin.list_display += ('phone_number',)

admin.site.register(Customer, UserAdmin)
