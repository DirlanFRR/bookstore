import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from order.factories import OrderFactory, UserFactory
from order.models import Order
from product.factories import CategoryFactory, ProductFactory


class TestOrderViewSet(APITestCase):

    def setUp(self):
        # Criando um usuário e autenticando-o
        self.user = UserFactory()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)  # Garantindo que as requisições sejam autenticadas

        # Criando uma categoria e produto corretamente
        self.category = CategoryFactory(title="technology")
        self.product = ProductFactory(title="mouse", price=100)
        self.product.category.set([self.category])  # Corrigindo o relacionamento ManyToMany

        # Criando um pedido associado ao usuário
        self.order = OrderFactory(user=self.user)
        self.order.product.set([self.product])  # Corrigindo o relacionamento ManyToMany

    def test_order(self):
        response = self.client.get(reverse("order-list", kwargs={"version": "v1"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

     
