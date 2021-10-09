from django.test import Client
from django.test import TestCase

from django.urls import reverse

from customers.models import Customer



class TestCustomerViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.customer = Customer.objects.create_user(username='Saeed', password='password')
        self.client.login(username='Saeed', password='password')
        self.sign_up_url = reverse('customers:sign_up')
        self.sign_in_url = reverse('customers:sign_in')
        self.change_password_url = reverse('customers:change_password')
        self.customer_profile_url = reverse('customers:profile')
        self.addresses_url = reverse('customers:addresses')
        self.delete_address_url = reverse('customers:delete_address', args=[1])
        self.orders_url = reverse('customers:orders')
        self.order_items_url = reverse('customers:order_items', args=[1])

    def test_sign_up_view_GET(self):
        response = self.client.get(self.sign_up_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('customers/sign_up.html')

    def test_sign_in_view_GET(self):
        response = self.client.get(self.sign_in_url)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('customers/sign_in.html')

    def test_change_password_view_GET(self):
        response = self.client.get(self.change_password_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('customers/sign_in.html')

    def test_customer_profile_view_GET(self):
        response = self.client.get(self.customer_profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('customers/customer_profile.html')

    def test_addresses_view_GET(self):
        response = self.client.get(self.addresses_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('customers/addresses.html')

    def test_orders_view_GET(self):
        response = self.client.get(self.orders_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('customers/orders.html')

    # def test_order_items_view_GET(self):
    #     response = self.client.get(self.order_items_url)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed('customers/sign_in.html')
