# def function_name(parameter1, parameter2, parameterX):
#     code line 1

def calculate_age(birth_year):
    print("You are {} years old".format(2026 - birth_year))

calculate_age(1996)

#example 1 - financial info for only 1 month
name = "Monthly balance - January"
row = {"Balance": 1200,
       "Income": 1800,
       "Expenses": 1300}

print("*" * 10)
print(name)
print("*" * 10)
for k, v in row.items():
    print("{} : {}".format(k, v))
print("*" * 10)

#example 2 - financial info for many months
rows = [
    ("January", {"Balance": 1200, "Income": 1800, "Expenses": 1300}),
    ("February", {"Balance": 2300,
                  "Income": 3000,
                  "Expenses": 900})
]

# name - month, row - financial info
for name_of_month, row_financial_info in rows:
    print("*" * 10)
    print("Monthly balance {}". format(name_of_month))
    print("*" * 10)
    for key, value in row_financial_info.items():
        print("{} : {}".format(key, value))
    print("*" * 10)

# #example 3 - financial info for many months and for the data owner
#
owner = {"First name": "Jan",
         "Last name": "Nowak"}

print("*" * 10)
print("Account owner")
print("*" * 10)
for key, value in owner.items():
    print("{} : {}".format(key, value))
print("*" * 10)

# name - month, row - financial info
for name_of_month, row_financial_info in rows:
    print("*" * 10)
    print("Monthly balance {}". format(name_of_month))
    print("*" * 10)
    for key, value in row_financial_info.items():
        print("{} : {}".format(key, value))
    print("*" * 10)



# # example 4 - simplify with functions
def divider(mul=10, char="*"):
    print(char * mul)

def print_dict(name, row):
    divider(20, "-")
    print(name)
    divider()
    for k, v in row.items():
        print("{} : {}".format(k, v))
    divider()

owner = {
    "First name": "Jan",
    "Last name": "Nowak"
}

rows = [
    ("January", {"Balance": 1200, "Income": 1800, "Expenses": 1300}),
    ("February", {"Balance": 2300,
                  "Income": 3000,
                  "Expenses": 900})
]
#
print_dict("Owner", owner)
#
# #name - month, row - financial info

#check gender in polish name
def get_gender(name):
    if name[-1] == "a":
        return "Female" #return - quit with value
    return "Male"

names = ["Marek", "Anna", "Ewa", "Jan"]
for first_name in names:
    print("{} is a {}" .format(first_name, get_gender(first_name)))

divider(20, "-")

def double_value(a): #wont work without a return
    a = a * 2

def double_values(row):
    for k, v in row.items():
        row[k] = v * 2

a = 10
print(id(a))
double_value(a) #pass integer (immutable)
print(a)

b = "Some string"
double_value(b) #pass string (immutable)
print(b)

sample_dict = {"a": 10, "b": "String"}
print(sample_dict)
double_values(sample_dict)
print(sample_dict)

sample_var = 10
print(id(sample_var)) #id returns address of the variable
sample_var = sample_var + 10 #variable is re-declared (brand new)
print(id(sample_var))

sample_string = "aaa"
print(id(sample_string))
sample_string = sample_string + "bbb"
print(id(sample_string))

sample_dict = {"a": 10}
print(id(sample_dict))
sample_dict["a"] += 10
print(id(sample_dict)) #id address is the same, not changing

#mutable value - you can change without relocation in memory:
#dictionary, list, set, objects

#immutable - change with relocation
#tuple, string, float, integer