#company account money value
current_account_balance = 200  # made-up number to start with something
action_with_money = 0
operations = []

#Possible commands of operation
commands = [
    "Balance",
    "Sale",
    "Purchase",
    "Account",
    "List",
    "Warehouse",
    "Review",
    "End"
]

warehouse = {
    "Lemon": {"Quantity": 100, "Price": 0.5},
    "Cauliflower": {"Quantity": 80, "Price": 0.7},
    "Basket": {"Quantity": 60, "Price": 8}
}

# FUNCTIONS:

#1 user choice from a list
def select_from_list(options, name):
    print("Select " + name + ":")
    for i, option in enumerate(options, start=1):
        print(f"{i}) {option}")

    while True:
        user_entry = input("Option: ")

        try:
            choice = int(user_entry) - 1

        except ValueError:
            print("Please write a number of the chosen " + name + ".")
            continue

        if 0 <= choice < len(options):
            print("You've chosen " + name + ":", options[choice])
            return options[choice]
        else:
            print("Please select a valid number")

#2 Balance command
def balance_command(current_account_balance, operations):
    print("Change the account balance. Write a negative number to remove money, positive to add.")

    try:
        newest_change = int(input("Amount: "))
    except ValueError:
        print("Please enter a number")
        return current_account_balance

    current_account_balance += newest_change
    operations.append(
        f"Balance changed by {newest_change}, new balance: {current_account_balance}"
    )
    print("Current balance:", current_account_balance)
    return current_account_balance

#keeping track of actions
def tracking_actions(current_account_balance, newest_change):
    current_account_balance += newest_change
    operations.append(
        f"Account balance changed by {newest_change}, new balance: {current_account_balance}")
    print("Current balance:", current_account_balance)
    return current_account_balance

#Sale command
def sale_command(warehouse, current_account_balance, operations):
    print("Choose an item from the list (1) or add a new item (2)")
    print("Available items:")
    for i, option in enumerate(warehouse, start=1):
        print(f"{i}) {option}")
    while True:
        old_or_new = input()
        if old_or_new == "1":
            item_chosen = select_from_list(list(warehouse.keys()), "item")
            item_sold = int(input("How many of the " + item_chosen + " item are you selling? "))
            warehouse[item_chosen]["Quantity"] -= item_sold

            current_account_balance += warehouse[item_chosen]["Price"] * item_sold
            operations.append(
                f"{item_sold} of {item_chosen} item sold, new account balance: {current_account_balance}. There are {warehouse[item_chosen]["Quantity"]} of {item_chosen} left in the warehouse."
            )
            print((
                f"{item_sold} of {item_chosen} item sold, new account balance: {current_account_balance}. There are {warehouse[item_chosen]["Quantity"]} of {item_chosen} left in the warehouse."))
            return current_account_balance
        elif old_or_new == "2":
            item_new_name = input("What's the name of the new item? ")
            item_new_price = int(input("What's the price of the new item? "))
            item_new_quantity = int(input("How many of the new item are you selling? "))
            warehouse.update({
                item_new_name: {
                    "Quantity": -item_new_quantity,
                    "Price": item_new_price}
            })
            current_account_balance += item_new_price * item_new_quantity
            return current_account_balance
        else:
            print("Choose available option")



# ---- ACTUAL APP

command_chosen = select_from_list(commands, "command")

if command_chosen == "Balance":
    current_account_balance = balance_command(current_account_balance, operations)

elif command_chosen == "Sale":
    current_account_balance = sale_command(warehouse, current_account_balance, operations)
    print(warehouse)

    # print("Select an item:")
    # for i, item in enumerate(warehouse, start=1):
    #     print(f"{i}) {item}")
    #
    # while True:
    #     user_entry = input("Item: ")
    #
    #     try:
    #         choice = int(user_entry) - 1
    #
    #     except ValueError:
    #         print("Please write a number of the chosen item")
    #         continue
    #
    #     if 0 <= choice < len(commands):
    #         print("You've chosen item:", warehouse[choice])
    #         return warehouse[choice]
    #     else:
    #         print("Please select a valid number")