from django.test import SimpleTestCase
from django.urls import reverse, resolve
from orders.views import basket_view, delete_item_from_basket, checkout


class TestOrdersUrls(SimpleTestCase):
    def test_basket_url_is_resolved(self):
        url = reverse('orders:basket')
        self.assertEqual(resolve(url).func, basket_view)

    def test_delete_item_from_basket_url_is_resolved(self):
        url = reverse('orders:delete_item_from_basket')
        self.assertEqual(resolve(url).func, delete_item_from_basket)

    def test_checkout_url_is_resolved(self):
        url = reverse('orders:checkout')
        self.assertEqual(resolve(url).func, checkout)
