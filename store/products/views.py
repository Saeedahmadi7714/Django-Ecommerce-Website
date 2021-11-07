from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
)


class IndexView(ListView):
    model = Product

    # 3 of the most visited products
    queryset = (Product.objects.filter(is_active=True, in_stock=True).annotate(product_view=Count('views')).order_by(
        '-product_view')[:3])

    context_object_name = 'products'
    template_name = 'products/index.html'

    # 5 of the latest products
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['latest'] = Product.objects.filter(
            is_active=True, in_stock=True).order_by('-created')[:5]
        return context


class ShopView(ListView):
    model = Product
    queryset = Product.objects.filter(
        is_active=True, in_stock=True).order_by('-created')[:9]
    context_object_name = 'products'
    template_name = 'products/shop.html'

    def get_context_data(self, **kwargs):
        context = super(ShopView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(is_active=True)
        return context


class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'products/product_detail.html'

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        product = get_object_or_404(Product, slug=slug)
        return product


def product_by_category(request, category):
    context = dict()
    category_id = Category.objects.get(name=category).id
    categories = Category.objects.filter(is_active=True)
    product_list = Product.objects.filter(
        category=category_id, is_active=True, in_stock=True)
    context['products'] = product_list
    context['categories'] = categories
    return render(request, 'products/product_by_category.html', context=context)


class AboutView(TemplateView):
    template_name = 'products/about.html'


class ContactView(TemplateView):
    template_name = 'products/contact.html'
