from django.urls import (path)

from .views import (SignUp, ChangePassword)

urlpatterns = [
    path('sign_up/', SignUp.as_view(), name='sign_up_api'),
    path('change_password/', ChangePassword.as_view(), name='change_password_api'),
]
