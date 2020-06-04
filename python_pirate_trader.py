import os
print("Welcome to Python Pirate Trader")

firm_name = input("Please enter your Firm Name: ")

print("Firm Name:  "+ firm_name)

starting_options = input("How do you wish to start. 1) Cash & Debt 2) Cannons no debt.: ")

if starting_options == "1":
    cash = 250
    debt = cash
    cannons = 0
else:
    cash = 0
    debt = 0
    cannons = 5

os.system("cls")
print("------------------------------")
print("Python Pirate Trader 0.1A")
print("------------------------------")
# print("Cash = " + cash)
