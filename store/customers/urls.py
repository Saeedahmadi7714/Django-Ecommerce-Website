from django.urls import path
from .views import (SignUpView, SigninView, logout_view,
                    customer_profile_view, dashboard_view, ChangePasswordView)

app_name = 'customers'

urlpatterns = [
    path('sign_up/', SignUpView.as_view(), name='sign_up'),
    path('sign_in/', SigninView.as_view(), name='sign_in'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('logout/', logout_view, name='logout'),
    path('profile/', customer_profile_view, name='profile'),
    path('dashboard/', dashboard_view, name='dashboard'),
]
