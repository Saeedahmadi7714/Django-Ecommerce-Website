from django.urls import path, include
from .views import SignUp

urlpatterns = [
    path('sign_up/', SignUp.as_view(), name='sign_up_api')
]
