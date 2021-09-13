from rest_framework import serializers
from customers.models import Customer


class SignUpSerializer(serializers.ModelSerializer):
    password_check = serializers.CharField(write_only=True, style={
        'input_type': 'password'
    })

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'username', 'password', 'password_check', 'email', 'phone_number',
                  'avatar', ]

        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self):
        new_customer = Customer(
            first_name=self._validated_data['first_name'],
            last_name=self._validated_data['last_name'],
            username=self._validated_data['username'],
            email=self._validated_data['email'],
            phone_number=self._validated_data['phone_number'],
            avatar=self.validated_data['avatar']
        )
        password = self.validated_data['password']
        password_check = self.validated_data['password_check']

        if password != password_check:
            raise serializers.ValidationError({
                'password': 'Passwords must match'
            })
        new_customer.set_password(password)
        new_customer.save()
        return new_customer
