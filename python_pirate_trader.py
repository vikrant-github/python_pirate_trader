import os
MENU_DIVIDER = "------------------------------"
GAME_TITLE = "Python Pirate Trader 0.1A"

def welcome_message():
    print("Welcome to Python Pirate Trader")

def get_firm_name():
    firm_name = input("Please enter your Firm Name: ")
    return firm_name

def get_starting_options():
    starting_options = input("How do you wish to start. 1) Cash & Debt 2) Cannons No debt. : ")
    if starting_options == "1":
        cash = 250
        debt = cash
        cannons = 0
    else:
        cash = 0
        debt = 0
        cannons = 5
    return cash, debt,cannons
   
# Start Game
welcome_message()
firm_name = get_firm_name()
cash,debt,cannons = get_starting_options()

# Display Main Game Interface
os.system("cls")
print(MENU_DIVIDER)
print(GAME_TITLE)
print(MENU_DIVIDER)

print("Firm Name: " + firm_name)
print("Cash: " + str(cash))
print("Debt: " + str(debt))
print("Cannons: " + str(cannons))