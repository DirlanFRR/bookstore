<<<<<<< HEAD
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
=======
from rest_framework.viewsets import ModelViewSet
>>>>>>> add226a540c144d1fe9bdbf578428686cf1acc60

from order.models import Order
from order.serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
<<<<<<< HEAD
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

=======

    serializer_class = OrderSerializer
>>>>>>> add226a540c144d1fe9bdbf578428686cf1acc60
    queryset = Order.objects.all().order_by("id")