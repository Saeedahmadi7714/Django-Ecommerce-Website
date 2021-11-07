from django.urls import path
from .views import (
    SignUpView, SigninView,
    logout_view, customer_profile_view,
    OrdersView, order_items_view,
    addresses_view, ChangePasswordView,
    DeleteUserAddress,
)

app_name = 'customers'

urlpatterns = [
    path('sign_up/', SignUpView.as_view(), name='sign_up'),
    path('sign_in/', SigninView.as_view(), name='sign_in'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('logout/', logout_view, name='logout'),
    path('profile/', customer_profile_view, name='profile'),
    path('addresses/', addresses_view, name='addresses'),
    path('delete_address/<int:pk>/',
         DeleteUserAddress.as_view(), name='delete_address'),
    path('orders/', OrdersView.as_view(), name='orders'),
    path('order_items/<int:order_id>/', order_items_view, name='order_items'),

]
