from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import FormView
from customers.forms import (SignUpForm, SignInForm,
                             CustomerProfileForm,
                             ChangePasswordForm,
                             AddressForm, )
from django.utils.translation import gettext_lazy as _

from customers.models import Address


class SignUpView(FormView):
    form_class = SignUpForm
    template_name = 'customers/sign_up.html'


class SigninView(LoginView):
    authentication_form = SignInForm
    redirect_field_name = 'next'
    template_name = 'customers/sign_in.html'
    redirect_authenticated_user = True


class ChangePasswordView(FormView):
    form_class = ChangePasswordForm
    template_name = 'customers/change_password.html'


@login_required
def customer_profile_view(request):
    if request.method == 'GET':

        context = dict()
        context['form'] = CustomerProfileForm(instance=request.user)
        return render(request, 'customers/customer_profile.html', context)

    elif request.method == 'POST':

        form = CustomerProfileForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()
            print(request.user.username)
            context = dict()
            context['form'] = CustomerProfileForm(instance=request.user)
            messages.success(request, _('Profile details updated successfully.'))
            return render(request, 'customers/customer_profile.html', context)

        return HttpResponse('Form invalid', form.errors)


@login_required
def addresses_view(request):
    context = dict()
    context['form'] = AddressForm()

    if request.method == 'GET':
        return render(request, 'customers/addresses.html', context)

    else:

        address_form = AddressForm(request.POST)
        if address_form.is_valid():

            user_addresses_in_database = Address.objects.filter(customer=request.user).count()
            print(user_addresses_in_database)

            if user_addresses_in_database >= 2:
                messages.error(request, 'You can not save new address.')
                return render(request, 'customers/addresses.html', context)
            else:
                new_address = Address(
                    customer=request.user,
                    address=address_form.cleaned_data['address'],
                    postcode=address_form.cleaned_data['postcode'],
                    city=address_form.cleaned_data['city'],
                    country=address_form.cleaned_data['country'],
                )
                new_address.save()
                messages.success(request, 'Your address saved.')
                return render(request, 'customers/addresses.html', context)

        messages.error(request, 'Form is invalid.')
        return render(request, 'customers/addresses.html', context)


def logout_view(request):
    logout(request)
    return redirect('products:index')
