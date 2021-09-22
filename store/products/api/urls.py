from django.urls import path
from .views import (CreateContactApi, ProductListApi)

urlpatterns = [
    path('contact/', CreateContactApi.as_view(), name='create_contact_api'),
    path('product_list/', ProductListApi.as_view(), name='product_list_api'),
]
