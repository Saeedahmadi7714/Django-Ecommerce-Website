from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from customers.models import Customer


class SignUpSerializer(serializers.ModelSerializer):
    password_check = serializers.CharField(write_only=True, style={
        'input_type': 'password'
    })

    class Meta:
        model = Customer
        fields = ['username', 'password', 'password_check', ]

        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self):
        new_customer = Customer(
            username=self._validated_data['username'],
        )
        password = self.validated_data['password']
        password_check = self.validated_data['password_check']

        if password != password_check:
            raise serializers.ValidationError({
                'password': _('Passwords must match'),
            })

        elif len(password) < 8:
            raise serializers.ValidationError({
                'password': _('Your password must be at least 8 characters long.')
            })

        new_customer.set_password(password)
        new_customer.save()
        return new_customer


class ChangePasswordSerializer(serializers.ModelSerializer):
    """
    Serializer for password change endpoint.
    """
    password = serializers.CharField(required=True, write_only=True, style={
        'input_type': 'password'
    })

    new_password = serializers.CharField(required=True, write_only=True, style={
        'input_type': 'password'
    })
    new_password_check = serializers.CharField(required=True, write_only=True, style={
        'input_type': 'password'
    })

    class Meta:
        model = Customer
        fields = ['password', 'new_password', 'new_password_check', ]

        extra_kwargs = {
            'password': {'write_only': True},
            'new_password': {'write_only': True},
            'new_password_check': {'write_only': True},
        }
