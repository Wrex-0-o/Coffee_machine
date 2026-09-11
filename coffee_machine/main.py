from art import gen_art
from recipe import MENU

def order(user_query):  
    if user_query in MENU:
        for ingredient in MENU[user_query]["ingredients"]:
            for on_hand in resources:
                if ingredient == on_hand and resources[on_hand] < MENU[user_query]["ingredients"][ingredient]:
                    print("Short on supplies!")
                    print(f"resource on hand: {on_hand}  MENU ingredient: {ingredient}")
                else:
                    print("Ready")


def coffee_machine():
    print(gen_art)

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
    "water" : 0,
    "milk" : 0,
    "coffee" : 0
}
money = 0
coffee_machine()