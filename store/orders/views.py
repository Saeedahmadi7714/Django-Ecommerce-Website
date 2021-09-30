from django.shortcuts import render

from products.models import Product


def basket_view(request):
    context = dict()
    if request.method == 'GET':

        if request.session.get('basket'):
            basket = request.session.get('basket')
            product_names = basket.keys()
            context['products_in_basket'] = Product.objects.filter(name__in=product_names)
            return render(request, 'orders/basket.html', context)
        else:
            return render(request, 'orders/basket.html')

    product_name = request.POST.get('product_name')
    product_quantity = request.POST.get('product_quantity')

    if not request.session.get('basket'):

        request.session['basket'] = {
            product_name: product_quantity
        }
        context['products_in_basket'] = Product.objects.filter(name=product_name)
        return render(request, 'orders/basket.html', context)

    else:

        basket = request.session.get('basket')
        basket[product_name] = product_quantity
        request.session.modified = True
        product_names = basket.keys()
        context['products_in_basket'] = Product.objects.filter(name__in=product_names)
        return render(request, 'orders/basket.html', context)
