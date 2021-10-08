from rest_framework import status
from rest_framework.exceptions import ErrorDetail
from rest_framework.test import APITestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from customers.api.views import SignUpView, ChangePasswordView

from customers.models import Customer


class TestSignUpApi(APITestCase):

    def test_sing_up_with_correct_data(self):
        data = {
            'username': 'Saeed',
            'password': 'password',
            'password_check': 'password'
        }
        response = self.client.post('/api/v1/sign_up/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_sign_up_with_do_not_match_passwords(self):
        data = {
            'username': 'Saeed',
            'password': 'password',
            'password_check': 'passwordpassword'
        }
        response = self.client.post('/api/v1/sign_up/', data)
        self.assertEqual(response.data['password'], 'Passwords must match')

    def test_sign_up_with_no_username(self):
        data = {
            'password': 'password',
            'password_check': 'password'
        }
        response = self.client.post('/api/v1/sign_up/', data)
        self.assertEqual(response.data['username'], [ErrorDetail(string='This field is required.', code='required')])

    def test_sign_up_with_blank_username(self):
        data = {
            'username': '',
            'password': 'password',
            'password_check': 'password'
        }
        response = self.client.post('/api/v1/sign_up/', data)
        self.assertEqual(response.data['username'], [ErrorDetail(string='This field may not be blank.', code='blank')])

    def test_sign_up_with_no_password(self):
        data = {
            'username': 'Saeed',
            'password_check': 'password'
        }
        response = self.client.post('/api/v1/sign_up/', data)
        self.assertEqual(response.data['password'], [ErrorDetail(string='This field is required.', code='required')])

    def test_sign_up_with_blank_password(self):
        data = {
            'username': 'Saeed',
            'password': '',
            'password_check': 'password'
        }
        response = self.client.post('/api/v1/sign_up/', data)
        self.assertEqual(response.data['password'], [ErrorDetail(string='This field may not be blank.', code='blank')])

    def test_sign_up_with_no_password_check(self):
        data = {
            'username': 'Saeed',
            'password': 'password',
        }
        response = self.client.post('/api/v1/sign_up/', data)
        self.assertEqual(
            response.data['password_check'],
            [ErrorDetail(string='This field is required.', code='required')]
        )

    def test_sign_up_with_blank_password_check(self):
        data = {
            'username': 'Saeed',
            'password': 'password',
            'password_check': ''
        }
        response = self.client.post('/api/v1/sign_up/', data)
        self.assertEqual(
            response.data['password_check'],
            [ErrorDetail(string='This field may not be blank.', code='blank')]
        )

    def test_sign_up_with_(self):
        data = {
            'username': 'Saeed',
            'password': 'pass',
            'password_check': 'pass'
        }
        response = self.client.post('/api/v1/sign_up/', data)
        print(response.data)
        self.assertEqual(
            response.data['password'],
            ErrorDetail(string='Your password must be at least 8 characters long.', code='invalid')
        )


class TestCustomerApiUrls(SimpleTestCase):

    def test_sign_up_api_url_is_resolved(self):
        url = reverse('sign_up_api')
        # class-based views need to be compared by name
        self.assertEqual(resolve(url).func.__name__, SignUpView.as_view().__name__)

    def test_change_password_api_url_is_resolved(self):
        url = reverse('change_password_api')
        self.assertEqual(resolve(url).func.__name__, ChangePasswordView.as_view().__name__)
