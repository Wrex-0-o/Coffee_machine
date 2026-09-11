from art import gen_art
from recipe import MENU

def make_coffee(order, charge):
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))

    total = round(quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01, 2)

    if total < charge:
        print("That's not Enough! Money refunded.")
        return
    else:
        change = round(total - charge, 2)
        print(f"Here's your change ${change} and your {order}!")
        return



def order(user_query):  
    if user_query in MENU:
        for ingredient in MENU[user_query]["ingredients"]:
            for on_hand in resources:
                if ingredient == on_hand and resources[on_hand] < MENU[user_query]["ingredients"][ingredient]:
                    print(f"Sorry there isn't enough {on_hand}.")
                    return              
    else:
        print("Sorry! That's not on the MENU.")
        return
    
    print(f"It's ${MENU[user_query]["cost"]} for {user_query}.")
    make_coffee(user_query, MENU[user_query]["cost"])
    return

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
            print(f"Water: {resources["water"]}ml \nMilk: {resources["milk"]}ml \nCoffee: {resources["coffee"]}g \nMoney: ${money}")
        else:
            order(user_query)


resources = {
    "water" : 300,
    "milk" : 200,
    "coffee" : 100
}
coffee_machine()