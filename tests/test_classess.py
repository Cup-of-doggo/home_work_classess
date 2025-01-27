from tests.test_product_attribute import some_product


def test_init_product(product_apple):
    assert product_apple.name == "Apple"
    assert product_apple.description == "red"
    assert product_apple.price == 99.9
    assert product_apple.quantity == 1000


def test_init_category(category_fruit):
    assert category_fruit.name == "fruits"
    assert category_fruit.description == "fruits from India"
    assert category_fruit.products == [str(some_product)]
    assert category_fruit.product_count == 1
    assert category_fruit.category_count == 2
