client_package_weight = 0
packages_sent = 0
unused_capacity_per_package = []  #recommended to use list (its like array)
max_unused_package = None
max_unused_capacity = 0

#ask user about what number of items to send.  (max_items)
print("How many items do you want to send?")
items_count = input()
#Best with while loop for this task (item_count < max_items)

while items_count < max_items:
    #ask about the weight of the current item
print("How much does the item weight?")
    current_package_weight = int(input())  #check if the weight == 0 and then break the loop
    if current_package_weight == 0:
        break
    elif current_package_weight >= 1 or <= 10:    #check if 1 <= weight <= 10
        #if yes start adding your item to the package (check if weight of the current package exceeded 20kg)
        current_package_weight > 20

#print the resultprint("How much does the item weight?")o
print(f"the package weights {current_package_weight}")