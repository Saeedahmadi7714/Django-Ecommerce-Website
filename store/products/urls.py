from django.urls import path
from .views import (IndexView, ShopView, ProductDetail, ProductByCategory)

app_name = 'products'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('products/<slug:slug>', ProductDetail.as_view(), name='product_detail'),
    path('category/<slug:slug>', ProductByCategory.as_view(), name='product_by_category'),
]
