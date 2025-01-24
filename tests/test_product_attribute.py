from src.product import Product


some_product = Product("corn", "vegetable", 100, 10)


def test_show():
    assert some_product.show == "corn, 100 руб. Остаток: 10 шт."


def test_new_product():
    new_product = Product.new_product({"name": "apple", "description": "fruit", "price": 180,
         "quantity": 15})
    assert new_product.show == 'apple, 180 руб. Остаток: 15 шт.'


def test_price():
    assert some_product.price == 100


def test_price_setter():
    some_product.price = 150
    assert some_product.price == 150