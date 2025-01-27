class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product):
        name = product['name']
        description =product['description']
        price = product['price']
        quantity = product['quantity']
        return cls(name, description, price, quantity)

    def __str__(self):
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price == 0 or new_price < 0:
            print('Цена не должна быть нулевая или отрицательная')
        else:
            self.__price = new_price

    def __add__(self,other):
        return self.__price * self.quantity + other.__price * other.quantity

    def quantity(self):
        return self.quantity
