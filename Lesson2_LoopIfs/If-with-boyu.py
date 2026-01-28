import sys
#if condition

a = 3

if a % 2 == 1:
    print("Number is odd")

if a % 2 == 1:
    print("Number is even")

a = True
b = False
c = a or b
if c:
    print("Condition true")

c = "simple string"
if c:
    print("This line will be executed")

c = ""
if c:
    print("This line will be skipped")


#if else condition

a = 3
if a % 2 == 1:
    print("Number is odd")
if a % 2 == 0:
    print("Number is even")

if a % 2 == 1:
    print("Number is odd")
else:
    print("Number is even")

#nested conditions in else block(fizzbuzz)

example = 15
if example % 5 and example % 3:
    print(example)
else:
    response = ""
    if example % 5 == 0:
        response = response + "Fizz"
    if example % 3 == 0:
        response = response + "Buzz"
    print(response)

#nested conditions in if block

if example % 5 == 0 or example % 3 == 0:
    response = ""
    if example % 5 == 0:
        response = response + "Fizz"
    if example % 3 == 0:
        response = response + "Buzz"
    print(response)
else:
    print(example)

#elif condition code

if example % 15 == 0:
    print("Fizzbuzz")
elif example % 5 == 0:
    print("Fizz")
elif example % 3 == 0:
    print("Buzz")
else:
    print(example)

#While loop
i = 0
while i < 10:
    print(f"iteration {i}")
    i = i + 1

#check if a number is prime
example = 24
x = example // 2
factor = 0
while x > 1:
    if  example % x == 0:
        print(f"{example} has factor {x}")
        factor = x
    x -= 1 #x = x - 1

if not factor:
    print(f"{example} is prime")
else:
    print(f"{example} is not prime")

#check if a number is prime - version with "is_prime" value
example = 20
x = example // 2
is_prime = True
while x > 1:
    if  example % x == 0:
        print(f"{example} has factor {x}")
        is_prime = False
    else:
        print(f"{example} DOESN'T have a factor {x}")
    x -= 1 #x = x - 1

if is_prime == True:
    print(f"{example} is prime")
else:
    print(f"{example} is not prime")

#break statement (with factorial)
counter = 0
product = 1
while counter < 10:
    counter += 1
    print(f"I'm calculating {counter}")
    product *= counter
    if product > 1000:
        break
    print(f"{counter}: {product}")

#check if a number is prime - v.2 from course
example = 2137
x = example // 2
factor = 0
while x > 1:
    if  example % x == 0:
        print(f"{example} is not prime")
        break
    x -= 1 #x = x - 1
else:
    print(f"{example} is prime")

#"for" loop - code to execute a given number of times
for i in range(10): #it's less than 10
    print(i)

print()

for i in range(5, 10):
    print(i)

print()

for i in range(0, 10, 2): #start, stop and step numbers in range
    print(i)

print()

#start loop at 10 and stop at 0. step has to be minus.
for i in range(10, 0, -1): #start, stop and step numbers in range
    print(i)

print()

for i in range(0, 10): #continue is a stupid command. It actually skips a step
    if i == 5:
        continue
    if i == 7:
        continue
    print(i)

#parameters
#print(sys.argv[0]) #first argument is reserved for a program name
#print(sys.argv[1]) #argument from terminal only
#print(sys.argv[2]) #whatever you input later

#WORKSHOP
#Flight can have max 20 people. cost of ticket for kid - 200, adult - 400. Adult can get wine for 10. Program has to calculate income. If age is 0 - break the loop
wine_count = 0
child_count = 0 # before the flight everything is 0
adult_count = 0
passenger_count = 0
#child_ticket = 200
#adult_ticket = 400

while passenger_count < 20:
    #ask passenger about age
    print("Enter passenger age")
    age = int(input())
    if age == 0:
        break
    elif age < 18:
        child_count += 1
        passenger_count += 1
        continue
    print("enter the number of glasses of wine")
    wine_current = int(input())
    if wine_current < 0 or wine_current > 3:
        print("wrong number of glasses of wine")
        continue
    wine_count += wine_current
    adult_count += 1
    passenger_count += 1

print("Adults: {}, Children: {}, Glasses of wine {}".format(
    adult_count,
    child_count,
    wine_count,
    adult_count * 400 + child_count * 200 + wine_count * 10
))

