MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}
# All cash
penny = 0.01
nickel = 0.05
dime = 0.1
quarter = 0.25
money = 0
total_cash = 0
remaining_change = 0

# Balance cash
quarters_qty = 0
dimes_qty = 0
nickles_qty = 0
pennies_qty = 0

def process_order(order,total_cash):
    global remaining_change
    if order == "report":
        print(f"Here's your report {resources}")
    elif order == "off":
        print("Turning off for maintenance")
    elif order =="espresso" or order == "latte" or order == "cappuccino":
        remaining_change = total_cash - MENU[order]["cost"]
        resources['money'] += MENU[order]["cost"]
        print(f"Here's your {order}")
        if remaining_change > 0:
            print(f"Here's your remaining change: {remaining_change}")
        elif remaining_change < 0:
            print(f"Amount insufficient for {order}")
    else:
        print("Invalid selection")

# def update_resources(order):
#     if order == "espresso":
#         resources["water"] -= MENU[order]["ingredients"]["water"]
#         resources["coffee"] -= MENU[order]["ingredients"]["coffee"]
#     elif order == "latte" or order == "cappuccino":
#         resources["water"] -= MENU[order]["ingredients"]["water"]
#         resources["milk"] -= MENU[order]["ingredients"]["milk"]
#         resources["coffee"] -= MENU[order]["ingredients"]["coffee"]

def update_resources(order):
    for ingredient in MENU[order]["ingredients"]:
        if ingredient == "water":
            resources[ingredient] -= MENU[order]["ingredients"][ingredient]

def take_cash():
    global total_cash
    print("Please insert coins.")
    quarters_qty = int(input("how many quarters?: "))
    dimes_qty = int(input("how many dimes?: "))
    nickles_qty = int(input("how many nickles?: "))
    pennies_qty = int(input("how many pennies?: "))
    total_cash = (quarters_qty * quarter) + (dimes_qty * dime) + (nickles_qty * nickel) + (
            pennies_qty * penny)
    print(f"You paid: ${total_cash}")
    return total_cash

# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
coffee_on = True
while coffee_on:
    order = input("What would you like? (espresso, latte, cappuccino): ")
    if order == "off":
        coffee_on = False

    # TODO: 5. Process coins.
    if order == "espresso" or order == "latte" or order == "cappuccino":
        if "milk" not in MENU[order]["ingredients"]:
            if (resources["water"] >= MENU[order]["ingredients"]["water"] and
                    resources["coffee"] >= MENU[order]["ingredients"]["coffee"]):
                take_cash()
                if total_cash >= MENU[order]["cost"]:
                    process_order(order, total_cash)
                    update_resources(order)
                    print(resources)
                else:
                    short_amount = MENU[order]["cost"] - total_cash
                    print(f"You are short ${short_amount}")
            elif (resources["water"] < MENU[order]["ingredients"]["water"] or
               resources["coffee"] < MENU[order]["ingredients"]["coffee"]):
                print(f"Sorry that's not enough resources.")
                if resources["water"] < MENU[order]["ingredients"]["water"]:
                    print(f"Refill water")
                if resources["coffee"] < MENU[order]["ingredients"]["coffee"]:
                    print(f"Refill coffee")

        elif "milk" in MENU[order]["ingredients"]:
            if (resources["water"] >= MENU[order]["ingredients"]["water"] and
                    resources["coffee"] >= MENU[order]["ingredients"]["coffee"] and
                    resources["milk"] >= MENU[order]["ingredients"]["milk"]):
                take_cash()
                if total_cash >= MENU[order]["cost"]:
                    process_order(order, total_cash)
                    update_resources(order)
                    print(resources)
                else:
                    short_amount = MENU[order]["cost"] - total_cash
                    print(f"You are short ${short_amount}")
            elif (resources["water"] < MENU[order]["ingredients"]["water"] or
               resources["coffee"] < MENU[order]["ingredients"]["coffee"] or
               resources["milk"] < MENU[order]["ingredients"]["milk"]):
                print(f"Sorry that's not enough resources.")
                if resources["water"] < MENU[order]["ingredients"]["water"]:
                   print(f"Refill water")
                if resources["coffee"] < MENU[order]["ingredients"]["coffee"]:
                   print(f"Refill coffee")
                if resources["milk"] < MENU[order]["ingredients"]["milk"]:
                   print(f"Refill milk")
        else:
            print("Refill resources")
            coffee_on = False
    elif order == "report":
        print(f"{resources}")
    elif order == "off":
        coffee_on = False
    else:
        print("Unknown drink")
        coffee_on = False


# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
