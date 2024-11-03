import factory
from product.models import Product, Category

class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('word')
    slug = factory.Faker('slug')
    description = factory.Faker('sentence')
    active = factory.Iterator([True, False])

    class Meta:
        model = Category


class ProductFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('word')
    price = factory.Faker('pyint')
    category = factory.SubFactory(CategoryFactory)  # Definindo a categoria com SubFactory

    class Meta:
        model = Product
