from django.utils.timezone import now
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from orders.models import Discount


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def offer_code_api_view(request):
    if request.method == 'POST':
        offer_code = request.POST.get('offerCode')
        customer = request.user
        try:
            discount = Discount.objects.get(code=offer_code)

            if discount.is_active and discount.expire_date > now() and discount.customer == customer:
                content = {'applied': 'Your discount code was applied correctly.',
                           'amount': discount.amount}
                discount.is_active = False
                discount.save()
                return Response(content, status=status.HTTP_200_OK)

            elif not discount.is_active:
                content = {'used': 'Your discount code has been used.'}
                return Response(content, status=status.HTTP_404_NOT_FOUND)

            elif discount.expire_date < now():
                content = {'expired': 'Your discount code has been used.'}
                return Response(content, status=status.HTTP_404_NOT_FOUND)

        except Discount.DoesNotExist:
            content = {'incorrect offer code': 'Your offer code is incorrect.'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
