from django.test import SimpleTestCase
from django.urls import reverse, resolve
from products.views import (
    IndexView, ShopView,
    ProductDetail, product_by_category,
    AboutView, ContactView
)


class TestProductsUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('products:index')
        # class-based views need to be compared by name
        self.assertEqual(resolve(url).func.__name__, IndexView.as_view().__name__)

    def test_shop_url_is_resolved(self):
        url = reverse('products:shop')
        self.assertEqual(resolve(url).func.__name__, ShopView.as_view().__name__)

    def test_product_detail_url_is_resolved(self):
        url = reverse('products:product_detail', args=['product_slug'])
        self.assertEqual(resolve(url).func.__name__, ProductDetail.as_view().__name__)

    def test_product_by_category_url_is_resolved(self):
        url = reverse('products:product_by_category', args=['category_name'])
        self.assertEqual(resolve(url).func, product_by_category)

    def test_about_url_is_resolved(self):
        url = reverse('products:about')
        self.assertEqual(resolve(url).func.__name__, AboutView.as_view().__name__)

    def test_contact_url_is_resolved(self):
        url = reverse('products:contact')
        self.assertEqual(resolve(url).func.__name__, ContactView.as_view().__name__)
