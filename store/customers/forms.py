from django.contrib.auth.forms import (AuthenticationForm, UserCreationForm, )
from django import (forms, )

from .models import (Customer, )


class SignUpForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['username', 'password', ]


SignUpForm = SignUpForm


class SignInForm(AuthenticationForm):
    class Meta:
        model = Customer


class ChangePasswordForm(forms.ModelForm):
    new_password = forms.CharField(max_length=150)
    new_password_confirm = forms.CharField(max_length=150)

    class Meta:
        model = Customer
        fields = ['password', 'new_password', 'new_password_confirm', ]


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone_number', ]
