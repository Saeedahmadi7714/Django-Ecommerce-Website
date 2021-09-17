from rest_framework import (serializers, )
from customers.models import (Customer, )
from django.utils.translation import gettext_lazy as _


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
