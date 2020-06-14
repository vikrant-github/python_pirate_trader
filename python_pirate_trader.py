import os
import datetime
import random

MENU_DIVIDER = "------------------------------"
GAME_TITLE = "Python Pirate Trader 0.1A"

def welcome_message():
    print("Welcome to Python Pirate Trader")

def get_firm_name():
    # firm_name = input("Please enter your Firm Name: ")
    return "Jack Sparrow Traders"

def get_starting_options():
    starting_options = input("How do you wish to start. 1) Cash & Debt 2) Cannons No debt. : ")
    if starting_options == "1":
        opts = (250, 250, 0)
    else:
        opts = (0, 0, 5)
    # Tuples is a list of data that cannot be changed
    return opts

def leave_port(city_list, current_date):
    i = 1
    for city in city_list:
        print("{0}) {1}".format(i, city.name))
        i += 1
    select_city = input('Which city do you wish to go to?: ')
    current_date += datetime.timedelta(days=1)
    return city_list[int(select_city) -1], current_date

def buy():
    input("What do you want to buy? ")

def sell():
    input("What do you want to sell? ")

def visit_bank():
    input("How much you want to transfer? ")

def display_products():
    for product in Product.products:
        print(product.name + "--" + str(product.price))
        
# Product Class
class Product(object):
    products = []
    # Constructor
    def __init__(self, name, minprice, maxprice):
        self.name = name
        self.minprice = minprice
        self.maxprice = maxprice
        self.price = random.randint(self.minprice, self.maxprice)
    @classmethod
    def create_products(cls):
        cls.products.append(Product("General Goods", 3, 20))
        cls.products.append(Product("Arms", 10, 75))

# Product Class
class City(object):
    cities = []
    # Constructor
    def __init__(self, name, has_warehouse, has_bank):
        self.name = name
        self.has_warehouse = has_warehouse
        self.has_bank = has_bank
        #self.price = random.randint(self.minprice, self.maxprice)
    @classmethod
    def create_cities(cls):
        cls.cities.append(City("Hong Kong", True, True))
        cls.cities.append(City("Shanghai", False, False))
        cls.cities.append(City("London", False, False))


# Create Products
Product.create_products()

# Create Cities
City.create_cities()

# Start Game
welcome_message()
firm_name = get_firm_name()
cash,debt,cannons = get_starting_options()
current_city = City.cities[0]
current_date  = datetime.datetime(1820,1,1)

game_running = True

while game_running:
    # Display Main Game Interface
    os.system("cls")
    print(MENU_DIVIDER)
    print(GAME_TITLE)
    print(MENU_DIVIDER)
    #Using String Formatting: 3 different ways of formatting other than concatenation
    print("Firm Name: %s" % firm_name)
    print("Cash: {:,}".format(cash)) # Better way of formatting
    print(f"Debt: {debt}" ) # Another way of formatting in Python 3.6 or above, fstrings or string interpolation
    print("Cannons: %d"  % cannons)
    print("City: %s" % current_city.name)
    # http://strftime.org 
    print("Date: {:%B %d, %Y}".format(current_date))
    print(MENU_DIVIDER)
    print("------City Products------")
    display_products()
    has_bank_string = ""
    if current_city.has_bank == True:
        has_bank_string = "V)isit Bank,"
    print("Menu L)eave Port, B)uy, S)ell, T)ransfer Warehouse, %s Q)uit" % has_bank_string)
    menu_option = input("What is your option: ")
    if menu_option == "L":
        current_city, current_date = leave_port(City.cities, current_date)
    elif menu_option == "B":
        buy()
    elif menu_option == "S":
        sell()
    elif menu_option == "V" and current_city.has_bank == True:
        visit_bank()
    elif menu_option == "Q":
        #break
        game_running = False
