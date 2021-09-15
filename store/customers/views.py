from django.contrib.auth import (logout, )
from django.contrib.auth.decorators import (login_required, )
from django.contrib.auth.views import (LoginView, )
from django.shortcuts import (redirect, render, )
from django.views.generic import (FormView, )
from customers.forms import (SignUpForm, SignInForm, CustomerProfileForm, )
from customers.models import (Customer, )


class SignUpView(FormView):
    form_class = SignUpForm
    template_name = 'customers/sign_up.html'


class SigninView(LoginView):
    authentication_form = SignInForm
    redirect_field_name = 'next'
    template_name = 'customers/sign_in.html'
    redirect_authenticated_user = True


@login_required
def customer_profile_view(request):
    if request.method == 'GET':
        context = dict()
        context['form'] = CustomerProfileForm(instance=request.user)
        return render(request, 'customers/customer_profile.html', context)


def dashboard_view(request):
    pass


def logout_view(request):
    logout(request)
    return redirect('products:product_list')
