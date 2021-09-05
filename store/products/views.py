from django.shortcuts import render
from django.views.generic import (ListView, DetailView)
from .models import (Product)


class ProductList(ListView):
    model = Product
    queryset = Product.objects.all(is_active=True)
    context_object_name = 'products'
    template_name = 'products/index.html'


class ProductDetail(DetailView):
    model = Product
    queryset = Product.objects.all(is_active=True)
    context_object_name = 'product'
    template_name = 'products/product_detail.html'


class ProductByCategory(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'products/product_by_category.html'
    queryset = Product.objects.all(is_active=True)

    def get_queryset(self):
        """Filter products by a category"""
        return self.queryset.filter(category=self.kwargs.get('slug'))