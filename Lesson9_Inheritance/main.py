import json

from Lesson9_Inheritance.DigitalProduct import MBRProduct
from Lesson9_Inheritance.Product import Product

p1 = Product("Prod1", 100)
print(p1)
p2 = Product("Prod2", 100)
print(p2)
p3 = Product("Prod2", 100)
print(p3)

print(p2.counter)

print(p1.id)
print(p2.id)
print(p3.id)

#Executing method using class names
print(Product.counter)
print(Product.get_price(p1, 10)) #p1 -> set to the "self"
print(p1.get_price(10)) #more common usage of function from the class

mbrp = MBRProduct("MBR", 100, 10)
print(mbrp.get_price(11))

#=========exceptions=========
# easy example 1:
# try:
#     integer_value = int(input("Provide number: "))
# except ValueError as e:
#     print("Please enter a number")
#     print(e)

#catching multiple possible errors
# try:
#     integer_1 = json.loads("{a")
# except json.decoder.JSONDecodeError as e:
#     integer_val1 = 0
#     print(e)
#
# try:
#     integer_2 = int(input("Provide number: "))
# except ValueError as e:
#     integer_val2 = 0
#     print(e)


# example of error in function
def function_with_error():
    for i in range(6):
        print("before: {}".format(i))
        integer_val3 = int(input("Provide number: "))
        print("after: {}".format(i))

try:
    function_with_error()
except ValueError as e:
    print(e)