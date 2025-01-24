class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        self.product_count += len(products)
        Category.category_count += 1

    @property
    def products(self):
        return self.__products


    def add_product(self,product: classmethod):
        self.product_count += 1
        return self.__products.append(product)
