import os
import datetime
from product import Product
from city import City
from game_manager import GameManager

def welcome_message():
    print("Welcome to Python Pirate Trader")

def get_firm_name():
    # firm_name = input("Please enter your Firm Name: ")
    return "Jack Sparrow Traders"

def get_starting_options():
    starting_options = input("How do you wish to start. 1) Cash & Debt 2) Cannons No debt. : ")
    if starting_options == "1":
        opts = (250, 2000, 0)
    else:
        opts = (0, 0, 5)
    # Tuples is a list of data that cannot be changed
    return opts

# Get Game Options
welcome_message()

firm_name = get_firm_name()

cash, debt, cannons = get_starting_options()

game = GameManager(shiphold=100, name=firm_name, cash=cash, debt=debt, cannons=cannons)  # Creating an instance of a Game Manager Class

# Start Up Game
game.start_up()