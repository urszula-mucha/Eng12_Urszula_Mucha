# message = "Hello"
# print(message)
#
# message = message + "World"
# print(message)
#
# #task 1
# age=2
# price=1.52
# name="Yolanda"
# print(type(age))
# print(type(price))
# print(type(name))
#
# #task 2
# a=15
# b=4
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)
# print(a**b)
#
# #task 3
# x=10
# print(x > 5)
# print(x <= 10)
# print(x != 7)
#
# #task 4
# temperature = 22
# print(temperature > 20 and temperature < 30)
# print(temperature < 0 or temperature > 35)
#
# #task 5
# a=12
# b=5
# task = a%b
# print(task==2 or task >= 3)
#
# #task 6 - check if number is even or odd
# number = int(input("provide number to check")) #everything what user inputs is string
# result = number % 2
# print("number is even {}".format(result == 0))
# print("number is odd {}".format(result == 1))

#task 7. Use ctrl + / to disable code You marked before
user_age = 16
ticket_price = 35

client_age = int(input("how old are you?"))
print("client can buy ticket, that's {}" .format(client_age >=16))
client_money = int(input("how rich are you?"))
print("client can afford ticket, that's {}" .format(client_money >=35))