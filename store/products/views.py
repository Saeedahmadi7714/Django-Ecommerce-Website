from django.views.generic import (ListView, DetailView)
from .models import (Product, Category)


class ProductList(ListView):
    model = Product
    queryset = Product.objects.filter(is_active=True)
    context_object_name = 'products'
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(is_active=True)
        return context


class ProductDetail(DetailView):
    model = Product
    queryset = Product.objects.filter(is_active=True)
    context_object_name = 'product'
    template_name = 'products/product_detail.html'


class ProductByCategory(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'products/product_by_category.html'
    queryset = Product.objects.filter(is_active=True)

    def get_queryset(self):
        """Filter products by a category"""
        return self.queryset.filter(category=self.kwargs.get('slug'))
