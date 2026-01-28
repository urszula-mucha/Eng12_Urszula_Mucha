
#starting status of the warehouse tracker
with open("current_account_balance.txt", "w") as file:
    file.write("200")
#current_account_balance = 200 #made-up number to start with something
action_with_client = 0

warehouse = {
    "apple": {"quantity": 100, "price": 0.5},
    "banana": {"quantity": 80, "price": 0.7},
    "basket": {"quantity": 60, "price": 8}
}

#operations = {
   # "Balance",
  #  "Sale",
 #   "Purchase",
   # "Account",
 #   "List",
#}

commands = {}
#     [USER OPTION] = PROGRAM RESULT
commands["Balance"] = "Balance"
commands["Sale"] = "Sale"
commands["Purchase"] = "Purchase"
commands["Account"] = "Account"
commands["List"] = "List"
commands["Warehouse"] = "Warehouse"
commands["Review"] = "Review"
commands["End"] = "End"

def selectFromDict(products, name):
    index = 0
    indexValidList = []
    print("Select a " + name + ":")
    for productName in products:
        index = index + 1
        indexValidList.extend([products[productName]])
        print(str(index) + ") " + productName)
    inputValid = False
    while not inputValid:
        inputRaw = input(name + ": ")
        inputNo = int(inputRaw) - 1
        if inputNo > -1 and inputNo < len(indexValidList):
            selected = indexValidList[inputNo]
            print("Selected " +  name + ": " + selected)
            inputValid = True
            break
        else:
            print("Please select a valid " + name + " number")
    return selected

products = {}
#     [USER OPTION] = PROGRAM RESULT
products["Dog food"] = "Balance"
products["Cat food"] = "Sale"
products["Pet carrier"] = "Purchase"
products["Kennel"] = "Account"


# Let user select a command
command = selectFromDict(commands, "command")



if command == "Balance":
    print("How much money did You make for the company? Write a negative number if you bought something, positive if you sold")
    action_with_client = int(input())
    print(current_account_balance + action_with_client)
elif command == "Sale":

    #def saleFunctions

    print("How many of these items did you buy?")
    # Let user select a product
    #product = selectFromDict(products, "product")
   # print("how many did you sell?")
    #action_with_client = int(input())
    items = list(warehouse.keys())

    for i, item in enumerate(items, start=1):
        print(f"{i}) {item}")
        choice = int(input("Select item: ")) - 1

    if 0 <= choice < len(items):
        selected_item = items[choice]
    #selected_item == "banana"  # for example
    print("Price:", warehouse[selected_item]["price"])
    print("Quantity:", warehouse[selected_item]["quantity"])