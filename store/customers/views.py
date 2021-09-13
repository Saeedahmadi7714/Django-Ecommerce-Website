from django.contrib import messages
from django.contrib.auth import (authenticate, login, logout)
from django.shortcuts import redirect, render
from django.views.generic import FormView

from customers.forms import (SignUpForm, SignInForm, )


class SignUpView(FormView):
    form_class = SignUpForm
    template_name = 'customers/sign_up.html'


def sign_in_view(request):
    if request.method == 'GET':
        context = dict()
        context['form'] = SignInForm
        return render(request, 'customers/sign_in.html', context)

    elif request.method == 'POST':

        form = SignInForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:

                if user.is_active:

                    login(request, user)
                    return redirect('products:product_list')
                else:

                    messages.warning(request, "Your account is disabled!")
                    return redirect('customers:sign_in')
            else:
                messages.warning(request, "The username or password are not valid!")

        return redirect('customers:sign_in')


def logout_view(request):
    logout(request)
    return redirect('products:product_list')
