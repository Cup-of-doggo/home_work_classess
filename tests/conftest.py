import pytest

from src.category import Category
from src.product import Product
from tests.test_product_attribute import some_product


@pytest.fixture
def product_apple():
    return Product("Apple", "red", 99.9, 1000)


@pytest.fixture
def category_fruit():
    return Category("fruits", "fruits from India", [some_product])
