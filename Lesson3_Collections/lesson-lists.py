#Lists, sets, tuples and dictionaries
# #lists are in square brackets
list_empty = []

#there can be different type of content in a single list
list1 = ["Marek", "John", 123, 40, True, False]

print(list1)

firstnames = ["Marek", "John", "Tom", "Jim", "Anna", "Mike"]
print(firstnames[0]) #shows items by their index
print(firstnames[1])

start_name_index = 2
print(firstnames[start_name_index])
print(firstnames[start_name_index + 2])
print(firstnames[-1]) #minus numbers in lists give You result from the backwards order

print(len(firstnames)) #length of the list

for index in range(6):
    print(index)

for index in [0, 1, 2, 3, 4, 5]:
    print(index)

for firstname in firstnames:
    print("name: {}".format(firstname))

#add another item to the list - it adds always at the end
firstnames.append("Jack")
print(firstnames)

#add something in the middle of the list
firstnames.insert(4, "Peter")
print(firstnames)

#add one list to another list
firstnames_female = ["Eve", "Anna"]
firstnames_male = ["Mark", "Peter", "Tom", "Jack"]
firstnames = firstnames_female + firstnames_male
print(firstnames)

#delete an item from list by index
del firstnames[2]
print(firstnames)

#delete by content
firstnames.remove("Tom")
print(firstnames)

firstnames = ["Mark", "John", "Tom", "Jim", "Tom", "Anna", "Mike", "Tom"]

firstnames.remove("Tom") #remove only first appearing content
print(firstnames)

#show the index of the first occurence
print(firstnames.index("Tom"))
#show the index of the first occurence from position 4
print(firstnames.index("Tom", 4))

#searching in collection
firstnames = ["Mark", "John", "Tom", "Jim", "Tom", "Anna", "Mike", "Tom"]
print(firstnames)
print(firstnames.index("Tom"))
print(firstnames.index("Tom", 3))
print(firstnames.index("Tom", 5))

if "Jacob" in firstnames:
    print("Name Jacob is in firstnames")
else:
    print("Name Jacob is not in firstnames")

#lists in boolean context
sample_list = []
print(bool(sample_list)) #empty list - it's false in bool
sample_list = ["a", "b"]
print(bool(sample_list)) #list with items - it's true in bool
sample_list = [""]
print(bool(sample_list)) #there is empty item in list but still something - true in bool

#if len(sample_list) > 0:
if sample_list:
    print("List has elements")
else:
    print("List has no elements")

#------------------------ TUPLES -----------------------------
#Tuples are faster, but You cant normally modify them

#like a list, but once declared You cant edit them. They use round brackets instead of square ones
sample_tuple = ("a", "b", 22, 0.4, False)
print(sample_tuple)

print(sample_tuple[3])
print(sample_tuple.index("a"))
print("a" in sample_tuple)

#Forbidden lines - they dont work
#sample_tuple.append("something")
#sample_tuple[0] = "queue"

#you can convert tuples to the list and back
sample_list = list(sample_tuple)
sample_list.append("something")
sample_tuple = tuple(sample_list)
print(sample_tuple)

#assigning multiple variables in one line using tuples
a, b = 1, 2
#its the same as doing a = 1 and b = 2
print(a)
print(b)

#You can build a list of tuples
fullnames = [
    ("John", "Doe"),
    ("Marek", "Wiśniewski"),
    ("Jan", "Kowalski")
]

#python can assign the names to values, because it recognizes the order
for firstname, lastname in fullnames:
    print(f"{firstname} {lastname}")

firstnames = ["Mark", "John", "Tom", "Jim", "Tom", "Anna", "Mike", "Tom"]
for index, firstnames in enumerate(firstnames):
    print("First name {}: {}".format(index + 1, firstname))

#hashable and id
a = 1
print(id(a)) #address in memory
a = 2
print(id(a)) #address in memory (ID) is different, because we redeclared the variable

#hashable (immutable): int, float, string, tuple, bool (only when contain immutable type). Lists are not!

#-------SETS--------
#in sets you are using unique values/ Written in curly braces
#You can't store list in the set, but You can store tuples - only hashable values
sample_set = {"a", "b", "sample_string", 1, 2, False, ("a", "b", "c")}
print(sample_set)

#add to set
sample_set.add("d")
print(sample_set)

#remove from set
sample_set.remove("b")
print(sample_set)

#check if element is in the set
print("a" in sample_set)
print("a" not in sample_set)

print(sample_set)

#print(sample_set[0]) won't work, because sets
#don't hold the orders so they dont have assigned ID to check the value by

sample_set_2 = {"a", "b", "c", "d"}
print(sample_set_2)

sample_set_2.add("d") #set doesn't give you an error hen the added object is duplicated

lst1 = list(sample_set)
print(lst1) #changed sets to lists can be recognized in terminal by the shape of the brackets

#------DICTIONARIES------
#storing pairs of key and value. Keys have to be unique, so kind of a set. Key has to be a hashable value.
sample_dictionary = {"a": 1,
                     "b": "string",
                     "c": 123,
                     "d": False,
                     2: "aaa"
                     }
print(sample_dictionary)

#in dictionary you have to look for values by the key,
#because dictionaries dont hold the order, just like the sets.

print(sample_dictionary["c"])
sample_dictionary["c"] = 456
print(sample_dictionary)

#print(sample_dictionary["x"]) when key doesnt exist then You'll get an error.

print(sample_dictionary.get("c"))

#check if key exists in dictionary
print("b" in sample_dictionary)
print("b" not in sample_dictionary)

#removing values
del sample_dictionary["c"]
print(sample_dictionary)

#iterate over dictionary
for k in sample_dictionary:
    print(" {}: {}".format(k, sample_dictionary[k]))

for k, v in sample_dictionary.items():
    print(" {}: {}".format(k, v))