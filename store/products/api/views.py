from rest_framework.generics import CreateAPIView
from .serializers import ContactSerializer


class CreateContactView(CreateAPIView):
    serializer_class = ContactSerializer
