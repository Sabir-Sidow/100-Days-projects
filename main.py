from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_money_machine = MoneyMachine()
my_coffe_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    user = input(f"What would you like? {options}").lower()
    if user == "off":
        is_on = False
    elif user == "report":
        my_coffe_maker.report()
        my_money_machine.report()
    else:
        drink = menu.find_drink(user)
        if my_coffe_maker.is_resource_sufficient(drink):
            if my_money_machine.make_payment(drink.cost):
                my_coffe_maker.make_coffee(drink)





