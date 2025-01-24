from src.category import Category

category_1 = Category("fruits", "fruits from India", ["banana", "mango"])
new_products = "apple"


def test_category_product():
    assert category_1.products ==  ["banana", "mango"]


def test_category_add_product():
    category_1.add_product(new_products)
    assert category_1.products == ["banana", "mango", "apple"]