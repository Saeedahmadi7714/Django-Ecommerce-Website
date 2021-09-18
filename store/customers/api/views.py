from rest_framework.generics import (CreateAPIView, UpdateAPIView, )
from rest_framework.permissions import (IsAuthenticated, )
from .serializers import (SignUpSerializer, ChangePasswordSerializer, )
from customers.models import (Customer, )
from rest_framework import status
from rest_framework.response import Response


class SignUpView(CreateAPIView):
    """
        Provides the possibility of registration
    """
    serializer_class = SignUpSerializer


class ChangePasswordView(UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = Customer
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):

        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Checking old password
            if not self.object.check_password(serializer.validated_data['password']):
                return Response({"password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

            # Checking new password length
            elif len(serializer.validated_data['new_password']) < 8:
                return Response({"new_password": ["Your password must be at least 8 characters long."]},
                                status=status.HTTP_400_BAD_REQUEST)
            # Checking new password and new password check

            elif serializer.validated_data['new_password'] != serializer.validated_data['new_password_check']:
                return Response({"passwords": ["New password and New password check must match."]},
                                status=status.HTTP_400_BAD_REQUEST)

            # If no error occurs, the password will be updated
            self.object.set_password(serializer.validated_data['new_password'])
            self.object.save()

            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
