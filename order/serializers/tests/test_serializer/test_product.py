import pytest
from order.models.product import Product  # Ajuste feito para importar de order.models.product

@pytest.mark.django_db
def test_create_product():
    product = Product.objects.create(
        title="Titulo teste do produto",
        description="Descrição de teste lalala",
        price=999
    )

    assert product.title == "Titulo teste do produto"
    assert product.description == "Descrição de teste lalala"
    assert product.price == 999
    assert product.id is not None