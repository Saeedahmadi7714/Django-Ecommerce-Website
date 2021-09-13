from django.urls import path
from .views import (SignUpView, sign_in_view, logout_view, )

app_name = 'customers'

urlpatterns = [
    path('sign_up/', SignUpView.as_view(), name='sign_up'),
    path('sign_in/', sign_in_view, name='sign_in'),
    path('logout/', logout_view, name='logout'),
]
