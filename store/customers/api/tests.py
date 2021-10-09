from django.test import SimpleTestCase
from django.urls import reverse, resolve
from rest_framework import status
from rest_framework.test import APITestCase

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

    def test_sing_up_with_short_length_username(self):
        data = {
            'username': 'Sa',
            'password': 'password',
            'password_check': 'password'
        }
        response = self.client.post('/api/v1/sign_up/', data)
        self.assertEqual(response.data['username'], 'Your username must be at least 3 characters long.')

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
        self.assertEqual(
            response.data['username'][0], 'This field is required.'
        )

    def test_sign_up_with_blank_username(self):
        data = {
            'username': '',
            'password': 'password',
            'password_check': 'password'
        }
        response = self.client.post('/api/v1/sign_up/', data)
        self.assertEqual(
            response.data['username'][0], 'This field may not be blank.'
        )

    def test_sign_up_with_no_password(self):
        data = {
            'username': 'Saeed',
            'password_check': 'password'
        }
        response = self.client.post('/api/v1/sign_up/', data)
        self.assertEqual(
            response.data['password'][0], 'This field is required.'
        )

    def test_sign_up_with_blank_password(self):
        data = {
            'username': 'Saeed',
            'password': '',
            'password_check': 'password'
        }
        response = self.client.post('/api/v1/sign_up/', data)
        self.assertEqual(
            response.data['password'][0], 'This field may not be blank.'
        )

    def test_sign_up_with_no_password_check(self):
        data = {
            'username': 'Saeed',
            'password': 'password',
        }
        response = self.client.post('/api/v1/sign_up/', data)
        self.assertEqual(
            response.data['password_check'][0],
            'This field is required.'
        )

    def test_sign_up_with_blank_password_check(self):
        data = {
            'username': 'Saeed',
            'password': 'password',
            'password_check': ''
        }
        response = self.client.post('/api/v1/sign_up/', data)
        self.assertEqual(
            response.data['password_check'][0],
            'This field may not be blank.'
        )

    def test_sign_up_with_short_length(self):
        data = {
            'username': 'Saeed',
            'password': 'pass',
            'password_check': 'pass'
        }
        response = self.client.post('/api/v1/sign_up/', data)
        self.assertEqual(
            response.data['password'],
            'Your password must be at least 8 characters long.'
        )


class TestCustomerApiUrls(SimpleTestCase):

    def test_sign_up_api_url_is_resolved(self):
        url = reverse('sign_up_api')
        # class-based views need to be compared by name
        self.assertEqual(resolve(url).func.__name__, SignUpView.as_view().__name__)

    def test_change_password_api_url_is_resolved(self):
        url = reverse('change_password_api')
        self.assertEqual(resolve(url).func.__name__, ChangePasswordView.as_view().__name__)


class TestChangePasswordApi(APITestCase):
    def setUp(self):
        Customer.objects.create_user(username='Saeed', password='password')
        self.client.login(username='Saeed', password='password')

    def test_change_password_api_with_correct_data(self):
        data = {
            'password': 'password',
            'new_password': 'newpassword',
            'new_password_check': 'newpassword'
        }
        response = self.client.put('/api/v1/change_password/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_change_password_api_with_incorrect_password(self):
        data = {
            'password': 'password2',
            'new_password': 'newpassword',
            'new_password_check': 'newpassword'
        }
        response = self.client.put('/api/v1/change_password/', data)
        self.assertEqual(response.data['password'][0], 'Wrong password.')

    def test_change_password_api_with_no_match_new_password_and_new_password_check(self):
        data = {
            'password': 'password',
            'new_password': 'newpassworddd',
            'new_password_check': 'newpassword'
        }
        response = self.client.put('/api/v1/change_password/', data)
        self.assertEqual(
            response.data['passwords'][0],
            'New password and New password check must match.')

    def test_change_password_api_with_no_new_password(self):
        data = {
            'password': 'password',
            'new_password_check': 'newpassword'
        }
        response = self.client.put('/api/v1/change_password/', data)
        self.assertEqual(
            response.data['new_password'][0],
            'This field is required.'
        )

    def test_change_password_api_with_blank_new_password(self):
        data = {
            'password': 'password',
            'new_password': '',
            'new_password_check': 'newpassword',
        }
        response = self.client.put('/api/v1/change_password/', data)
        self.assertEqual(
            response.data['new_password'][0],
            'This field may not be blank.'
        )

    def test_change_password_api_with_no_new_password_check(self):
        data = {
            'password': 'password',
            'new_password': '',
        }
        response = self.client.put('/api/v1/change_password/', data)
        self.assertEqual(
            response.data['new_password_check'][0],
            'This field is required.'
        )

    def test_change_password_api_with_blank_new_password_check(self):
        data = {
            'password': 'password',
            'new_password': 'newpassword',
            'new_password_check': ''
        }
        response = self.client.put('/api/v1/change_password/', data)
        self.assertEqual(
            response.data['new_password_check'][0],
            'This field may not be blank.'
        )

    def test_change_password_api_with_short_length(self):
        data = {
            'password': 'password',
            'new_password': 'new',
            'new_password_check': 'new'
        }
        response = self.client.put('/api/v1/change_password/', data)
        self.assertEqual(
            response.data['new_password'][0],
            'Your password must be at least 8 characters long.'
        )
