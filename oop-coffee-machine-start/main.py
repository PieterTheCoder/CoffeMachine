from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
menu = Menu()
on_off = True


while on_off:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}) ")
    if choice == "off":
        on_off = False
    elif choice == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffe_maker.make_coffee(drink)