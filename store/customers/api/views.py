from rest_framework.generics import (CreateAPIView, UpdateAPIView, )

from .serializers import (SignUpSerializer, )


class SignUp(CreateAPIView):
    """
        Provides the possibility of registration
    """
    serializer_class = SignUpSerializer


class ChangePassword(UpdateAPIView):
    """
    End point for changing user password
    """
