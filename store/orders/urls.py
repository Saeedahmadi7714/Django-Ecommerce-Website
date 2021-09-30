from django.urls import path

from orders.views import basket_view, delete_item_from_basket, checkout

app_name = 'orders'

urlpatterns = [
    path('basket/', basket_view, name='basket'),
    path('basket/delete/', delete_item_from_basket, name='delete_item_from_basket'),
    path('checkout/', checkout, name='checkout'),
]
