import tempfile

from django.test import TestCase
from products.models import IPaddress, Category, Product, Contact


class TestIPaddressModel(TestCase):
    def setUp(self):
        self.ip_address = IPaddress.objects.create(ip_address='127.0.0.1')

    def test_ip_address_is_created(self):
        self.assertEqual(str(self.ip_address), '127.0.0.1')


class TestCategoryModel(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='first_category', slug='first-category')

    def test_category_is_created(self):
        self.assertEqual(str(self.category), 'first_category')
        self.assertEqual(self.category.slug, 'first-category')
        self.assertEqual(self.category.is_active, True)


class TestProductModel(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='first_category', slug='first-category')
        self.ip_address = IPaddress.objects.create(ip_address='127.0.0.1')

        self.product = Product.objects.create(
            name='product1',
            slug='product1',
            category=self.category,
            description='Some description.',
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            number_of_product=15,
            price=150,

        )
        self.product.views.add(self.ip_address)

    def test_product_is_created(self):
        self.assertEqual(str(self.product), 'product1')
        self.assertEqual(self.product.is_active, True)
        self.assertEqual(self.product.in_stock, True)


class TestContactModel(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(
            name='Saeed', email='saeed@gmail.com', subject='Some message subject.',
            message='Some message.'
        )

    def test_category_is_created(self):
        self.assertEqual(str(self.contact), 'Saeed')
