from django.test import TestCase
from customers.models import Customer, Address


class TestCustomerModel(TestCase):
    def setUp(self):
        customer = Customer.objects.create(
            username='Saeed',
            first_name='Saeed',
            last_name='ahmadi',
            phone_number='09308150414',
            email='saeed@gmail.com'
        )
        customer.set_password('password')

    def test_customer_is_created(self):
        customer = Customer.objects.get(username='Saeed')
        self.assertEqual(str(customer), 'Saeedahmadi')


class TestAddressModel(TestCase):

    def setUp(self):
        customer = Customer.objects.create(
            username='Saeed',
            first_name='Saeed',
            last_name='ahmadi',
            phone_number='09308150414',
            email='saeed@gmail.com'
        )
        customer.set_password('password')

        Address.objects.create(
            customer=customer,
            address='1407 Rainbow Drive',
            country='USA',
            state='Ohio',
            city='Youngstown',
            postcode='44512'
        )

    def test_address_is_created(self):
        address = Address.objects.get(id=1)
        self.assertEqual(str(address), '1407 Rainbow Drive')
        self.assertEqual(address.address_type, 'home')
