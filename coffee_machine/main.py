from art import gen_art
from recipe import MENU

def make_coffee(order, charge, money):
    print("Please insert coins.")
    try:
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickels = int(input("How many nickels? "))
        pennies = int(input("How many pennies? "))
    except ValueError:
        print("You entered a Non-Numerical Input.")
        money -= charge
        return money

    total = round(quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01, 2)
    if total < charge:
        print("That's not Enough! Money refunded.\n")
        money -= charge
        return money
    else:
        for item in resources:
            if item in MENU[order]["ingredients"]:
                resources[item] = resources[item] - MENU[order]["ingredients"][item]
        change = round(total - charge, 2)
        print(f"Here's your change ${change} and your ☕ {order}!\n")
        return money



def order(user_query, money):  
    need_a_refill = []
    if user_query in MENU:
        for ingredient in MENU[user_query]["ingredients"]:
            for on_hand in resources:
                if ingredient == on_hand and resources[on_hand] < MENU[user_query]["ingredients"][ingredient]:
                    need_a_refill.append(ingredient)          
        if need_a_refill != []:
            print(f"Sorry there isn't enough {need_a_refill}.\n")
            return money
    else:
        print(f"Sorry! {user_query.title()} is not on the MENU.\n")
        return money

    money += MENU[user_query]["cost"]
    print(f"\nIt's ${MENU[user_query]["cost"]} for {user_query}.\n")
    money = make_coffee(user_query, MENU[user_query]["cost"], money)
    return money



def coffee_machine():
    print(gen_art)
    money = 0

    machine_on = True
    while machine_on:
        user_query = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_query == "off":
            print("Thank you for using our machine!")
            machine_on = False
        elif user_query == "report":
            print(f"\nWater: {resources["water"]}ml \nMilk: {resources["milk"]}ml \nCoffee: {resources["coffee"]}g \nMoney: ${money}\n")
        else:
            money = order(user_query, money)


resources = {
    "water" : 300,
    "milk" : 200,
    "coffee" : 100
}
coffee_machine()