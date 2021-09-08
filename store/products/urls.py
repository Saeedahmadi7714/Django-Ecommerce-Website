from django.urls import path
from .views import (ProductList, ProductDetail, ProductByCategory)

app_name = 'products'

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('products/<slug:slug>', ProductDetail.as_view(), name='product_detail'),
    path('category/<slug:slug>', ProductByCategory.as_view(), name='product_by_category'),
]
