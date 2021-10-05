from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from customers.models import Address
from orders.models import Discount, Order
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
    if request.method == 'GET':
        context = dict()
        customer = request.user
        addresses = Address.objects.filter(customer=customer)
        basket = request.session.get('basket')
        total_price = sum(
            [Product.objects.get(name=product_name).price * quantity for product_name, quantity in basket.items()])
        context['total_price'] = total_price
        context['addresses'] = addresses
        return render(request, 'orders/checkout.html', context)

    print(request.POST)

    # If the user has an address registered in the database and uses it to pay an order
    if 'address_id' in request.POST:
        basket = request.session.get('basket')
        delivery_method = request.POST.get('delivery_method')
        total_price = sum(
            [Product.objects.get(name=product_name).price * quantity for product_name, quantity in
             basket.items()]).amount

        if delivery_method == 'standard':
            total_price = total_price
        elif delivery_method == 'expedited':
            total_price += 15
        elif delivery_method == 'priority':
            total_price += 30

        customer = request.user
        address = Address.objects.get(id=request.POST.get('address_id'))

        # If user have an offer code
        if request.POST.get('offer_code'):
            discount = Discount.objects.get(code=request.POST.get('offer_code'))
            total_price_with_discount = (total_price * int(discount.amount)) / 100
            total_price_with_discount = total_price - total_price_with_discount
        else:
            discount = None
            total_price_with_discount = total_price

        order = Order(
            customer=customer,
            address=address,
            delivery_method=delivery_method,
            total_price=total_price,
            discount=discount,
            total_price_with_discount=total_price_with_discount
        )
        order.save()

        [order.products.create(product_name=product_name, quantity=quantity) for product_name, quantity in
         basket.items()]

        del request.session['basket']
        return render(request, 'orders/checkout_complete.html')

    # If the user has no address registered in the database
    elif 'address' in request.POST:
        basket = request.session.get('basket')
        delivery_method = request.POST.get('delivery_method')
        total_price = sum(
            [Product.objects.get(name=product_name).price * quantity for product_name, quantity in
             basket.items()]).amount

        if delivery_method == 'standard':
            total_price = total_price
        elif delivery_method == 'expedited':
            total_price += 15
        elif delivery_method == 'priority':
            total_price += 30

        customer = request.user

        # Create a new address and use it in the payment
        # Default address type is HOME

        new_address = Address(
            customer=customer,
            address=request.POST.get('address'),
            country=request.POST.get('country'),
            city=request.POST.get('city'),
            state=request.POST.get('state'),
            postcode=request.POST.get('postcode'),

        )
        new_address.save()
        # If user have an offer code
        if request.POST.get('offer_code'):
            discount = Discount.objects.get(code=request.POST.get('offer_code'))
            total_price_with_discount = (total_price * int(discount.amount)) / 100
            total_price_with_discount = total_price - total_price_with_discount
        else:
            discount = None
            total_price_with_discount = total_price

        order = Order(
            customer=customer,
            address=new_address,
            delivery_method=delivery_method,
            total_price=total_price,
            discount=discount,
            total_price_with_discount=total_price_with_discount
        )
        order.save()

        [order.products.create(product_name=product_name, quantity=quantity) for product_name, quantity in
         basket.items()]

        del request.session['basket']
        return render(request, 'orders/checkout_complete.html')
