from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

"""Checks if resources are enough"""
coffee_maker = CoffeeMaker()

money_machine = MoneyMachine()

menu = Menu()
# menu_item = MenuItem()


machine_on = True
while machine_on:
    options = menu.get_items()
    order_name = input (f"What would you like to do? {options}: ")
    if order_name == "off":
        machine_on = False
    elif order_name == "report":
        coffee_maker.report()
        money_machine.report()
        machine_on = True
    else:
        drink = menu.find_drink(order_name)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        else:
            menu.find_drink(drink)


