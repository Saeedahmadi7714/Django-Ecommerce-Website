from django.test import SimpleTestCase
from django.urls import reverse, resolve
from customers.views import (
    SignUpView, SigninView, ChangePasswordView,
    customer_profile_view, addresses_view, DeleteUserAddress,
    OrdersView, order_items_view, logout_view
)


class TestUrls(SimpleTestCase):

    def sign_up_url_is_resolved(self):
        url = reverse('customers:sign_up')
        self.assertEqual(resolve(url).func, SignUpView)
