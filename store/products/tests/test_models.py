import tempfile

from django.test import TestCase
from products.models import IPaddress, Category, Product, Contact


class TestIPaddressModel(TestCase):
    def setUp(self):
        IPaddress.objects.create(ip_address='127.0.0.1')

    def test_ip_address_is_created(self):
        ip_address = IPaddress.objects.get(id=1)
        self.assertEqual(str(ip_address), '127.0.0.1')


class TestCategoryModel(TestCase):
    def setUp(self):
        Category.objects.create(name='first_category', slug='first-category')

    def test_category_is_created(self):
        category = Category.objects.get(id=1)
        self.assertEqual(str(category), 'first_category')
        self.assertEqual(category.slug, 'first-category')
        self.assertEqual(category.is_active, True)


class TestProductModel(TestCase):
    def setUp(self):
        category = Category.objects.create(name='first_category', slug='first-category')
        ip_address = IPaddress.objects.create(ip_address='127.0.0.1')

        product = Product.objects.create(
            name='product1',
            slug='product1',
            category=category,
            description='Some description.',
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            number_of_product=15,
            price=150,

        )
        product.views.add(ip_address)

    def test_product_is_created(self):
        product = Product.objects.get(id=1)
        self.assertEqual(str(product), 'product1')
        self.assertEqual(product.is_active, True)
        self.assertEqual(product.in_stock, True)


class TestContactModel(TestCase):
    def setUp(self):
        Contact.objects.create(
            name='Saeed', email='saeed@gmail.com', subject='Some message subject.',
            message='Some message.'
        )

    def test_category_is_created(self):
        contact = Contact.objects.get(id=1)
        self.assertEqual(str(contact), 'Saeed')
