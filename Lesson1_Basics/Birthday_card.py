# Getting the info from a customer
print("Who are you writing to?")
recipient = input()
print("What year were you born?")
year = input()
print("What message do you want to send?")
message = input()
print("What's Your name?")
your_name = input()

#process the customer input
age = 2025 - int(year)

#print the message
print(f" {recipient}, let's celebrate your {age} years of awesomeness! \n Wishing you a day filled with joy and laughter as you turn {age}!\n ")
print(message)
print("\nWith love and best wishes,")
print(your_name)