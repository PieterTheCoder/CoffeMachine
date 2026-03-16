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
}
def recourses_sufficient(order_ingredients):
    """Returns True if the ingredients are sufficient to make a coffee
    and return false if the ingredients are not sufficient."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}. ")
            return False
    return True

def check_coins():
    """Return the total price of the drink"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def check_payment(money_received, drink_cost):
    if money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change: {change}")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry the money is not enough, Money refunded.")
        return False

def make_coffe(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ️️️️️️☕")

money = 0
on_off_machine = True
#TODO 1: Print report
while on_off_machine:
    coffe_check = input("What would you like? (espresso/latte/cappuccino): ")
    if coffe_check == "report":
        water_machine = resources["water"]
        milk_machine = resources["milk"]
        coffe_machine = resources["coffee"]
        money_machine = money
        print(f"Water: {water_machine}ml\nMilk: {milk_machine}ml\nCoffee: {coffe_machine}g\nMoney: {money_machine}$")

    elif coffe_check == "off":
        on_off_machine = False

    else:
        drink = MENU[coffe_check]
        if recourses_sufficient(drink["ingredients"]):
            payment = check_coins()
            check_payment(payment, drink["cost"])
            make_coffe(coffe_check, drink["ingredients"])

    #TODO 2: Check resources sufficient?
    #TODO 3: Process coins
    #TODO 4: Check transaction successful?
    #TODO 5: Make coffe