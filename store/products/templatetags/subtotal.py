"""
This module is for calculating the subtotal price in user basket
"""

from django import template

register = template.Library()


@register.simple_tag()
def subtotal_calculator(product_price, quantity, *args, **kwargs):
    return product_price * quantity
