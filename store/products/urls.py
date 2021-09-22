from django.urls import path
from .views import (IndexView, ShopView,
                    ProductDetail, product_by_category,
                    AboutView, ContactView)

app_name = 'products'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('products/<slug:slug>/', ProductDetail.as_view(), name='product_detail'),
    path('categories/<str:category>/', product_by_category, name='product_by_category'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
]
