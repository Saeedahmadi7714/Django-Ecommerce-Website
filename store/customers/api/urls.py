from django.urls import path
from .views import (SignUpView, ChangePasswordView, )

urlpatterns = [
    path('sign_up/', SignUpView.as_view(), name='sign_up_api'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password_api'),
]
