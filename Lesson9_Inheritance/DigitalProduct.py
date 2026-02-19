from datetime import datetime, timedelta
from math import ceil


# #digital products, we send at the moment we receive the payment
# class DigitalProduct:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def get_price(self, qty):
#         return self.price * qty
#
#     def available_at(self):
#         return datetime.now()
#
#     def __str__(self):
#         return self.name
#
# #Standard product. Sent in package
# class StandardProduct:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def get_price(self, qty):
#         return self.price * qty
#
#     def available_at(self):
#         return datetime.now() + timedelta(days=7)
#
#     def __str__(self):
#         return self.name
#
# #Product sold in rolls, e.g. wallpaper
# class MBRProduct:
#     def __init__(self, name, price, roll_size):
#         self.name = name
#         self.price = price
#         self.roll_size = roll_size
#
#     def get_price(self, qty):
#         return self.price * ceil(qty / self.roll_size)
#
#     def available_at(self):
#         return datetime.now() + timedelta(days=10)
#
#     def __str__(self):
#         return "{} {}".format(self.name, self.roll_size)

#There is a better way to wrote a similar classes - creating a base class and derived classes
#Base class product
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self,qty):
        return self.price * qty

    def __str__(self):
        return self.name

class DigitalProduct(Product):
    def available_at(self):
        return datetime.now()

class StandardProduct(Product):
    def available_at(self):
        return datetime.now() + timedelta(days=7)

class MBRProduct(Product):
    def __init__(self, name, price, roll_size):
        super().__init__(name, price)
        self.roll_size = roll_size

    def get_price(self, qty):
        return self.price * ceil(qty / self.roll_size)

    def available_at(self):
        return datetime.now() + timedelta(days=10)