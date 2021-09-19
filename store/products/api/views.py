from rest_framework.generics import CreateAPIView
from .serializers import ContactSerializer


class CreateContactView(CreateAPIView):
    """
        Provides the possibility of registration
    """
    serializer_class = ContactSerializer
