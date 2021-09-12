from django.forms import ModelForm
from .models import Customer


class SignUpForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'phone_number', 'avatar', ]


SignUpForm = SignUpForm


class SignInForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['username', 'password', ]


SignInForm = SignInForm
