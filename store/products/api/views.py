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

    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True)
        category = self.request.query_params.get('category')
        if category is not None:
            queryset = queryset.filter(category__name=category)
        return queryset
