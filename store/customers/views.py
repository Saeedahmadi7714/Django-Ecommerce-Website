from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, DeleteView
from customers.forms import (
    SignUpForm, SignInForm,
    CustomerProfileForm,
    ChangePasswordForm,
    AddressForm,
)
from django.utils.translation import gettext_lazy as _

from customers.models import Address
from orders.models import Order


class SignUpView(FormView):
    form_class = SignUpForm
    template_name = 'customers/sign_up.html'


class SigninView(LoginView):
    authentication_form = SignInForm
    redirect_field_name = 'next'
    template_name = 'customers/sign_in.html'
    redirect_authenticated_user = True


class ChangePasswordView(LoginRequiredMixin, FormView):
    form_class = ChangePasswordForm
    template_name = 'customers/change_password.html'


@login_required
def customer_profile_view(request):
    if request.method == 'GET':

        context = dict()
        context['form'] = CustomerProfileForm(instance=request.user)
        return render(request, 'customers/customer_profile.html', context)

    elif request.method == 'POST':

        form = CustomerProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            context = dict()
            context['form'] = CustomerProfileForm(instance=request.user)
            messages.success(request, _('Profile details updated successfully.'))
            return render(request, 'customers/customer_profile.html', context)

        return HttpResponse('Form invalid', form.errors)


@login_required
def addresses_view(request):
    context = dict()
    user_addresses_in_database = Address.objects.filter(customer=request.user)
    context['form'] = AddressForm()
    context['addresses'] = user_addresses_in_database

    if request.method == 'GET':
        return render(request, 'customers/addresses.html', context)

    else:
        address_form = AddressForm(request.POST)

        if address_form.is_valid():
            obj, created = Address.objects.update_or_create(

                # Get address if exist
                id=request.POST.get('address_id'),

                # Create or update address
                defaults={'customer': request.user,
                          'address': address_form.cleaned_data['address'],
                          'country': address_form.cleaned_data['country'],
                          'state': address_form.cleaned_data['state'],
                          'city': address_form.cleaned_data['city'],
                          'postcode': address_form.cleaned_data['postcode'],
                          'address_type': address_form.cleaned_data['address_type'],
                          },
            )

            if created:
                messages.success(request, 'Your address has been saved.')
            else:
                messages.success(request, 'Your address successfully updated.')

            return render(request, 'customers/addresses.html', context)

        messages.error(request, 'Form is invalid.')
        return render(request, 'customers/addresses.html', context)


class DeleteUserAddress(DeleteView):
    model = Address
    success_url = reverse_lazy('customers:addresses')


class OrdersView(LoginRequiredMixin, ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'customers/orders.html'

    def get_queryset(self):
        queryset = super(OrdersView, self).get_queryset()
        queryset = queryset.filter(customer=self.request.user)
        return queryset


@login_required
def order_products_view(request, order_id):
    if request.method == 'GET':
        context = dict()
        order_products = Order.objects.get(pk=order_id)
        context['products'] = order_products
        return render(request, 'customers/order_items.html', context)


def logout_view(request):
    logout(request)
    return redirect('products:index')
