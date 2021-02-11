import data
from data import MENU, resources, coins

menu = MENU

altered_resources = {
    "water": 0,
    "milk": 0,
    "coffee": 0,
    "money": resources["money"]
}



def check_resources(user_input):
    if user_input != "report":
        if count == 0:
            if altered_resources["water"] == 0 :
                pass
        if count > 0:
            if altered_resources != MENU[user_input]["ingredients"]:
                print("Brak matsow na kawe")



def user_money():
    user_coins = 0
    quarters = int(input("How many quarters? :>"))
    user_coins += coins["quarter"] * quarters
    dimes = int(input("How many dimes? :>"))
    user_coins += coins["dime"] * dimes
    nickles = int(input("How many nickles? :>"))
    user_coins += coins["nickle"] * nickles
    pennies = int(input("How many pennies? :>"))
    user_coins += coins["penny"] * pennies
    return user_coins


def check_transaction():
    if user_coins >= menu[user_input]["cost"]:
        return True
    else:
        return False


def manage_resources(user_input):
    altered_resources["water"] = resources["water"] - MENU[user_input]["ingredients"][
        "water"]
    altered_resources["milk"] = resources["milk"] - MENU[user_input]["ingredients"][
        "milk"]
    altered_resources["coffee"] = resources["coffee"] - MENU[user_input]["ingredients"][
        "coffee"]
    altered_resources["money"] = resources["money"] + MENU[user_input]["cost"]

    return altered_resources["water"], altered_resources["milk"], altered_resources["coffee"], altered_resources[
        "money"]


def calculate_change(user_input):
    if user_input == "report":
        return None
    else:
        change = user_coins - menu[user_input]["cost"]
        return f"${change} here is your change"


def print_resources():
    if count == 0:
        water = resources["water"]
        milk = resources["milk"]
        coffee = resources["coffee"]
        money = resources["money"]
        print(f"water : {water} ml\n milk: {milk} ml\n coffee : {coffee}g \n money : {money} $ ")
    else:
        water = altered_resources["water"]
        milk = altered_resources["milk"]
        coffee = altered_resources["coffee"]
        money = altered_resources["money"]
        print(f"water : {water} ml\n milk: {milk} ml\n coffee : {coffee}g \n money : {money} $ ")


count = 0
coffee = True
while coffee:
    user_input = str(input("What would you like? (espresso/latte/cappuccino):> "))
    check_resources(user_input)
    if user_input == "report":
        print_resources()
    elif user_input != "report":
        print("Please insert coins")
        user_coins = user_money()
        check = check_transaction()
        if check != False:
            manage_resources(user_input)
            count += 1
            print(f"Transaction passed, here is your {user_input}")
            print(calculate_change(user_input))
        else:
            print("Transaction failed, money returned")


