from django.test import TestCase
from django.utils.timezone import now
from customers.models import Customer, Address
from orders.models import Discount, OrderItem, Order


class TestDiscountModel(TestCase):
    def setUp(self):
        customer = Customer.objects.create(
            username='Saeed', first_name='Saeed', last_name='ahmadi'
        )
        customer.set_password('password')

        Discount.objects.create(
            customer=customer, code='DiscountCode', amount=30, expire_date=now()
        )

    def test_discount_is_created(self):
        discount = Discount.objects.get(id=1)
        self.assertEqual(str(discount), 'Saeedahmadi 30%')
        self.assertEqual(discount.is_active, True)


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
        customer = Customer.objects.create(
            username='Saeed', first_name='Saeed', last_name='ahmadi'
        )
        customer.set_password('password')

        address = Address.objects.create(
            customer=customer,
            address='1407 Rainbow Drive',
            country='USA',
            state='Ohio',
            city='Youngstown',
            postcode='44512'
        )

        order_item_1 = OrderItem.objects.create(product_name='product1', quantity=1)
        order_item_2 = OrderItem.objects.create(product_name='product2', quantity=2)
        order_item_3 = OrderItem.objects.create(product_name='product3', quantity=3)

        order = Order.objects.create(
            customer=customer,
            address=address,
            delivery_method='standard',
            total_price=154
        )

        order.products.add(order_item_1)
        order.products.add(order_item_2)
        order.products.add(order_item_3)

    def test_order_is_created(self):
        order = Order.objects.get(id=1)
        order_products_count = order.products.count()
        self.assertEqual(str(order), 'Saeedahmadi')
        self.assertEqual(order_products_count, 3)
        self.assertEqual(order.status, 'ready_to_ship')
