from rest_framework.generics import UpdateAPIView
from orders.api.serializers import DiscountSerializer
from orders.models import Discount


class OfferCodeApiView(UpdateAPIView):
    serializer_class = DiscountSerializer
    queryset = Discount.objects.get(is_active=True)
