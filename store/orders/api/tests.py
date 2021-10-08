from datetime import timedelta

from django.utils.timezone import now
from rest_framework.test import APITestCase

from customers.models import Customer
from orders.models import Discount

from django.test import SimpleTestCase
from django.urls import resolve, reverse
from orders.api.views import offer_code_api_view


class TestOfferCodeUpApi(APITestCase):
    def setUp(self):
        self.customer = Customer.objects.create_user(username='Saeed', password='password')
        expire_date = now() + timedelta(days=1)
        self.discount = Discount.objects.create(
            customer=self.customer, code='Davinci', amount=25, expire_date=expire_date
        )
        self.client.login(username='Saeed', password='password')

    def test_offer_code_with_correct_data(self):
        data = {
            'offerCode': 'Davinci',
        }
        response = self.client.post('/api/v1/offer_code/', data)
        self.assertEqual(
            response.data['applied'], 'Your discount code was applied correctly.'
        )
        self.assertEqual(
            response.data['amount'], self.discount.amount
        )

    def test_offer_code_with_incorrect_data(self):
        data = {
            'offerCode': 'Dainis',
        }
        response = self.client.post('/api/v1/offer_code/', data)
        self.assertEqual(
            response.data['incorrect offer code'], 'Your offer code is incorrect.'
        )

    def test_offer_code_with_used_code(self):
        self.discount.is_active = False
        self.discount.save()

        data = {
            'offerCode': 'Davinci',
        }
        response = self.client.post('/api/v1/offer_code/', data)
        self.assertEqual(
            response.data['used'], 'Your discount code has been used.'
        )

    def test_offer_code_with_expired_code(self):
        self.discount.expire_date -= timedelta(days=3)
        self.discount.save()

        data = {
            'offerCode': 'Davinci',
        }
        response = self.client.post('/api/v1/offer_code/', data)
        self.assertEqual(
            response.data['expired'], 'Your discount code has been used.'
        )


class TestOrderApiUrls(SimpleTestCase):

    def test_offer_code_api_url_is_resolved(self):
        url = reverse('offer_code_api')
        self.assertEqual(resolve(url).func, offer_code_api_view)
