from django.urls import path
from .views import OfferCodeApiView

urlpatterns = [
    path('offer_code/', OfferCodeApiView.as_view(), name='offer_code_api'),
]
