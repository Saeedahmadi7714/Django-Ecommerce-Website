from rest_framework.generics import CreateAPIView
from .serializers import SignUpSerializer


class SignUp(CreateAPIView):
    """
        Provides the possibility of registration
    """
    serializer_class = SignUpSerializer
