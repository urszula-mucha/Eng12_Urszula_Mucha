cats_set = ("Kaja", "Romek", "Ruby", "Brownie", "Naruto", "St00pka", "Nora", "Julka",
        "Dziecko", "Mario", "Lola", "Kr00vka", "Filip", "Maxi", "Millie"
            )
print(cats_set)
print(len(cats_set))

for cat in cats_set:
    print(cat)

for index, cat in enumerate(cats_set):
    print("Cat {}: {}".format(index + 1, cat))

#1 step: Define list with duplicates
#2 step: Check if list contains duplicates
#3 step: Print deduplicated collection

food = ["Smilla", "Catessy", "Whiskas", "Smilla", "Animonda"]
food_set = set(food)
print(len(food) - len(food_set))
print(food_set)

#task1: declare a list of sets (e. g. firstname, lastname)
#task2:iterate over collection

#fav_brand = list(food_set) + list(cats_list)

fav_brand = [
        ("Mario", "Catessy"),
        ("Mario", "Smilla"),
        ("Ruby", "Whiskas"),
        ("Julka", "Animonda")
    ]
for cat, brand in fav_brand:
        print(f"{cat} {brand}")

#task1: Reuse a list
#task2: Print only elements with only 5 characters or longer

#cats_list = list(cats_set) - actually set works as well, so I decided not to convert set to list
for cat in cats_set:
    if len(cat) >= 5:
        print(cat)

