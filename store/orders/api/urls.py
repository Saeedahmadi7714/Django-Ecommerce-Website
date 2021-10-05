from django.urls import path
from .views import offer_code_api_view

urlpatterns = [
    path('offer_code/', offer_code_api_view, name='offer_code_api'),
]
