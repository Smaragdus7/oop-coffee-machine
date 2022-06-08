from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Objects construction
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    options = menu.get_items()
    instruction = input(f"What would you like? {options}: ")
    if instruction == "off":
        is_on = False
    elif instruction == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(instruction)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

