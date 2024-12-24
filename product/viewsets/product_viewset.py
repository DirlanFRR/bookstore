from rest_framework.viewsets import ModelViewSet
<<<<<<< HEAD
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
=======
>>>>>>> add226a540c144d1fe9bdbf578428686cf1acc60

from product.models import Product
from product.serializers.product_serializer import ProductSerializer

<<<<<<< HEAD

class ProductViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by("id")
=======
class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()
>>>>>>> add226a540c144d1fe9bdbf578428686cf1acc60
