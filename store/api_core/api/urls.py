from django.urls import path, include

urlpatterns = [
    path('', include('customers.api.urls')),
    path('', include('products.api.urls')),
    path('', include('orders.api.urls')),
]
