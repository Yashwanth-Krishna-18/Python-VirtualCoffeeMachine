# DATA OF COFFEE MACHINE 
import math
import random

coffee_machine = {
    'espresso': {
        'ingredients': {"coffee": 100, 'water': 1000, 'milk': 0},
        "cost": 1.5
    },
    'cappuccino': {
        'ingredients': {"coffee": 150, 'water': 1000, 'milk': 250},
        "cost": 2.5
    },
    'latte': {
        'ingredients': {"coffee": 179, 'water': 1000, 'milk': 300},
        "cost": 2.5
    },
}

profit = 0
resources = {"water": 2000, "milk": 3000, "coffee": 650}

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕ Enjoy!")


def is_transaction_successful(money_received, drink_cost):
    """Return True if payment is accepted, or False if not enough money."""
    if money_received >= drink_cost:
        change = round((money_received - drink_cost), 2)
        print(f"Here is your change: ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def process_coins():
    """Return the total amount of money inserted."""
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickels = int(input("How many nickels? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    total = quarters + dimes + nickels + pennies
    return total


def is_resource_sufficient(order_ingredients):
    """Returns True if enough resources, False if not."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, not enough {item}.")
            return False
    return True


# Coffee Machine Loop
is_on = True
while is_on:
    choice = input("What would you like? (espresso/cappuccino/latte): ").lower()
    
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}\n")
    elif choice in coffee_machine:
        drink = coffee_machine[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print("Invalid choice. Please select espresso, cappuccino, or latte.")

# Let me know if you want to add more features or improve anything else! 🚀
