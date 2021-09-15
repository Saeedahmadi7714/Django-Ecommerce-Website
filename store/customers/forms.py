from django.contrib.auth.forms import (AuthenticationForm, UserCreationForm, )
from django import (forms, )

from .models import (Customer, )


class SignUpForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'phone_number', 'avatar', ]


SignUpForm = SignUpForm


class SignInForm(AuthenticationForm):
    class Meta:
        model = Customer


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'username', 'email', 'phone_number', 'avatar', ]
