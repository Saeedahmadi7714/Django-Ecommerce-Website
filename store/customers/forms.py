from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from .models import Customer, Address


class SignUpForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['username', 'password', ]


SignUpForm = SignUpForm


class SignInForm(AuthenticationForm):
    class Meta:
        model = Customer


class ChangePasswordForm(forms.ModelForm):
    password = forms.CharField(max_length=150, required=True, widget=forms.PasswordInput())
    new_password = forms.CharField(max_length=150, required=True, widget=forms.PasswordInput())
    new_password_check = forms.CharField(max_length=150, required=True, widget=forms.PasswordInput())

    class Meta:
        model = Customer
        fields = ['password', 'new_password', 'new_password_check', ]


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone_number', ]


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ['customer', 'created_at', 'updated_at', 'is_default']
