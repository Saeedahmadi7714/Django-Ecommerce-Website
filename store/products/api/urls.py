from django.urls import path
from .views import (CreateContactView, )

urlpatterns = [
    path('contact/', CreateContactView.as_view(), name='create_contact_api'),
]
