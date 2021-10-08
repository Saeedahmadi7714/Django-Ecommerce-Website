from rest_framework import status
from rest_framework.test import APITestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from products.api.views import CreateContactApi, ProductListApi


class TestCreateContactApi(APITestCase):

    def test_contact_with_correct_data(self):
        data = {
            'name': 'Saeed',
            'email': 'saeed@gmail.com',
            'subject': 'Test',
            'message': 'Some message for test.'
        }
        response = self.client.post('/api/v1/contact/', data)
        self.assertEqual(
            response.data,
            {'name': 'Saeed', 'email': 'saeed@gmail.com', 'subject': 'Test', 'message': 'Some message for test.'}
        )

    def test_contact_with_no_subject(self):
        data = {
            'name': 'Saeed',
            'email': 'saeed@gmail.com',
            'message': 'Some message for test.'
        }
        response = self.client.post('/api/v1/contact/', data)
        self.assertEqual(
            response.data['subject'][0],
            'This field is required.'
        )

    def test_contact_with_blank_subject(self):
        data = {
            'name': 'Saeed',
            'subject': '',
            'email': 'saeed@gmail.com',
            'message': 'Some message for test.'
        }
        response = self.client.post('/api/v1/contact/', data)
        self.assertEqual(
            response.data['subject'][0],
            'This field may not be blank.'
        )

    def test_contact_with_no_message(self):
        data = {
            'name': 'Saeed',
            'subject': 'Test',
            'email': 'saeed@gmail.com',
        }
        response = self.client.post('/api/v1/contact/', data)
        self.assertEqual(
            response.data['message'][0],
            'This field is required.'
        )

    def test_contact_with_blank_message(self):
        data = {
            'name': 'Saeed',
            'subject': 'Test',
            'email': 'saeed@gmail.com',
            'message': ''
        }
        response = self.client.post('/api/v1/contact/', data)
        self.assertEqual(
            response.data['message'][0],
            'This field may not be blank.'
        )


class TestProductListApi(APITestCase):

    def test_products_list(self):
        response = self.client.get('/api/v1/product_list/?page=1')
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


class TestProductsApiUrls(SimpleTestCase):

    def test_create_contact_api_url_is_resolved(self):
        url = reverse('create_contact_api')
        self.assertEqual(resolve(url).func.__name__, CreateContactApi.as_view().__name__, )

    def test_product_list_api_url_is_resolved(self):
        url = reverse('product_list_api')
        self.assertEqual(resolve(url).func.__name__, ProductListApi.as_view().__name__, )
