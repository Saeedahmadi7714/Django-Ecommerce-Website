from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from products.models import Product


def basket_view(request):
    """
    Provides the ability to add products to the basket as well as view the basket
    """
    context = dict()
    if request.method == 'GET':

        if request.session.get('basket'):
            basket = request.session.get('basket')
            product_names = basket.keys()
            context['products_in_basket'] = Product.objects.filter(name__in=product_names)
            return render(request, 'orders/basket.html', context)
        else:
            # Empty basket
            return render(request, 'orders/basket.html')

    product_name = request.POST.get('product_name')
    product_quantity = request.POST.get('product_quantity')

    if not request.session.get('basket'):
        number_of_products_is_stock = Product.objects.get(name=product_name).number_of_product
        if int(product_quantity) > number_of_products_is_stock or int(product_quantity) > 100:
            messages.error(request, 'More than inventory.')
            # Empty basket
            return render(request, 'orders/basket.html')

        # Adding product to the basket for the first time
        request.session['basket'] = {
            product_name: product_quantity
        }
        context['products_in_basket'] = Product.objects.filter(name=product_name)
        return render(request, 'orders/basket.html', context)

    else:
        # Update the basket or add new items to the basket
        basket = request.session.get('basket')
        number_of_products_is_stock = Product.objects.get(name=product_name).number_of_product

        if int(product_quantity) > number_of_products_is_stock or int(product_quantity) > 100:
            product_names = basket.keys()
            messages.error(request, 'More than inventory.')
            context['products_in_basket'] = Product.objects.filter(name__in=product_names)
            return render(request, 'orders/basket.html', context)

        # Add new item to basket
        basket[product_name] = product_quantity
        request.session.modified = True
        product_names = basket.keys()
        messages.success(request, 'Your basket has been updated.')
        context['products_in_basket'] = Product.objects.filter(name__in=product_names)
        return render(request, 'orders/basket.html', context)


def delete_item_from_basket(request):
    """
    Takes the product ID and removes it from the basket
    """
    if request.method == 'POST':
        product_name = Product.objects.get(pk=request.POST.get('productId'))
        basket = request.session.get('basket')
        basket.pop(str(product_name))
        request.session.modified = True
        return HttpResponse('Item deleted')


@login_required
def checkout(request):
    print(request.session.get('basket'))
    return HttpResponse('Fuck You :D')
