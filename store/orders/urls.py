from django.urls import path

from orders.views import basket_view

app_name = 'orders'

urlpatterns = [
    path('basket/', basket_view, name='basket')
]
