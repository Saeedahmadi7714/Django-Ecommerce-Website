from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from customers.models import Customer


class LoginRegisterTest(TestCase):

    # def testRegister(self):
    #     self.user = Customer.objects.create(
    #         username='maktab',
    #         first_name='Saeed',
    #         last_name='ahmadi',
    #         email="saeed@gmail.com",
    #     )
    #     self.user.set_password(12345678)
    #     self.user.save()
    #     assert Customer.objects.count() == 2

    def testSignUpView(self):
        response = self.client.post(reverse('customers:sign_in'),
                                    data={'username': 'admin2',
                                          'first_name': 'Saeed',
                                          'last_name': 'ahmadi',
                                          'email': 'saeed@gmail.com',
                                          'password': 12345678,
                                          'password_check': 12345678})
        self.assertEqual(response.status_code, 200)
