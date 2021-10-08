from django.test import TestCase
from django.utils.timezone import now
from customers.models import Customer, Address
from orders.models import Discount, OrderItem, Order


class TestDiscountModel(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create_user(
            username='Saeed', first_name='Saeed', last_name='ahmadi', password='password'
        )

        self.discount = Discount.objects.create(
            customer=self.customer, code='DiscountCode', amount=30, expire_date=now()
        )

    def test_discount_is_created(self):
        self.assertEqual(str(self.discount), 'Saeedahmadi 30%')
        self.assertEqual(self.discount.is_active, True)


class TestOrderItemModel(TestCase):
    def setUp(self):
        OrderItem.objects.create(product_name='product1', quantity=1)
        OrderItem.objects.create(product_name='product2', quantity=2)
        OrderItem.objects.create(product_name='product3', quantity=3)

    def test_order_items_are_created(self):
        order_item_count = OrderItem.objects.all().count()
        self.assertEqual(order_item_count, 3)


class TestOrderModelModel(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create_user(
            username='Saeed', first_name='Saeed', last_name='ahmadi', password='password'
        )

        self.address = Address.objects.create(
            customer=self.customer,
            address='1407 Rainbow Drive',
            country='USA',
            state='Ohio',
            city='Youngstown',
            postcode='44512'
        )

        order_item_1 = OrderItem.objects.create(product_name='product1', quantity=1)
        order_item_2 = OrderItem.objects.create(product_name='product2', quantity=2)
        order_item_3 = OrderItem.objects.create(product_name='product3', quantity=3)

        self.order = Order.objects.create(
            customer=self.customer,
            address=self.address,
            delivery_method='standard',
            total_price=154
        )

        self.order.products.add(order_item_1)
        self.order.products.add(order_item_2)
        self.order.products.add(order_item_3)

    def test_order_is_created(self):
        order_products_count = self.order.products.count()
        self.assertEqual(str(self.order), 'Saeedahmadi')
        self.assertEqual(order_products_count, 3)
        self.assertEqual(self.order.status, 'ready_to_ship')
