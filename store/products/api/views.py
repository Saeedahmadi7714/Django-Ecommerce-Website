from rest_framework.generics import (CreateAPIView,
                                     ListAPIView, )
from .serializers import ContactSerializer, ProductListSerializer
from rest_framework.pagination import PageNumberPagination
from ..models import Product


class CreateContactApi(CreateAPIView):
    serializer_class = ContactSerializer


class ProductListApi(ListAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductListSerializer
    pagination_class = PageNumberPagination
