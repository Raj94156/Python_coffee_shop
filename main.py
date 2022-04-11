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

# TODO 1: Prompt user by asking “​What would you like? (espresso/latte/cappuccino):"
while
user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()

# TODO 2: Print Report
money = 0
if user_choice == "report":
    print(f"Water : {resources['water']}ml")
    print(f"Milk : {resources['milk']}ml")
    print(f"Coffee : {resources['coffee']}g")
    print(f"Money : ${money}")

# TODO 3: Check the resorces
res = list(MENU.keys())[0]

res1 = list(MENU["espresso"]['ingredients'].keys())[0]
# res2 = MENU[res]
# print(MENU[])
print(MENU['espresso']['ingredients']['water'])
print(res)
if user_choice == str(res):
    print("helo")
def check_resources(user_option):


check_resources(user_choice)