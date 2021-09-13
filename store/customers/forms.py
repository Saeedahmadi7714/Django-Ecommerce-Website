from django import forms
from .models import Customer
from django.utils.translation import gettext_lazy as _


class SignUpForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'phone_number', 'avatar', ]


SignUpForm = SignUpForm


class SignInForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(label='Password', max_length=150, widget=forms.PasswordInput)
    widgets = {
        'password': forms.PasswordInput(),
    }


SignInForm = SignInForm
