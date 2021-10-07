from django.test import SimpleTestCase
from django.urls import reverse, resolve
from customers.views import (
    SignUpView, SigninView, ChangePasswordView,
    customer_profile_view, addresses_view, DeleteUserAddress,
    OrdersView, order_items_view, logout_view
)


class TestCustomersUrls(SimpleTestCase):

    def test_sign_up_url_is_resolved(self):
        url = reverse('customers:sign_up')
        # class-based views need to be compared by name
        self.assertEqual(resolve(url).func.__name__, SignUpView.as_view().__name__)

    def test_sign_in_url_is_resolved(self):
        url = reverse('customers:sign_in')
        self.assertEqual(resolve(url).func.__name__, SigninView.as_view().__name__)

    def test_change_password_url_is_resolved(self):
        url = reverse('customers:change_password')
        self.assertEqual(resolve(url).func.__name__, ChangePasswordView.as_view().__name__)

    def test_logout_url_is_resolved(self):
        url = reverse('customers:logout')
        self.assertEqual(resolve(url).func, logout_view)

    def test_profile_url_is_resolved(self):
        url = reverse('customers:profile')
        self.assertEqual(resolve(url).func, customer_profile_view)

    def test_address_url_is_resolved(self):
        url = reverse('customers:addresses')
        self.assertEqual(resolve(url).func, addresses_view)

    def test_delete_address_url_is_resolved(self):
        url = reverse('customers:delete_address', args=[1])
        self.assertEqual(resolve(url).func.__name__, DeleteUserAddress.as_view().__name__)

    def test_order_url_is_resolved(self):
        url = reverse('customers:orders')
        self.assertEqual(resolve(url).func.__name__, OrdersView.as_view().__name__)

    def test_order_items_url_is_resolved(self):
        url = reverse('customers:order_items', args=[1])
        self.assertEqual(resolve(url).func, order_items_view)
