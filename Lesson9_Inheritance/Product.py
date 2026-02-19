class Product:

    counter = 0 #staticproperty - the same for all objects

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.id = Product.counter
        Product.counter += 1

    def __str__(self):
        return self.name

    def get_price(self, qty):
        return self.price * qty