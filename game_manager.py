from city import City
from product import Product
import os
import datetime

MENU_DIVIDER = "------------------------------"
GAME_TITLE = "Python Pirate Trader 0.1A"

class GameManager(object):
    def __init__(self, **kwargs):
        self.firm_name = kwargs['name']
        self.cash = kwargs['cash']
        self.debt = kwargs['debt']
        self.cannons = kwargs['cannons']
        self.bank = 0
        self.shiphold = kwargs['shiphold']
        # Create Products
        Product.create_products()
        # Create Cities
        City.create_cities()
        self.current_city = City.cities[0]
        self.current_date  = datetime.datetime(1820,1,1)
    
    def leave_port(self, city_list, current_date):
        i = 1
        for city in city_list:
            print("{0}) {1}".format(i, city.name))
            i += 1
        select_city = input('Which city do you wish to go to?: ')
        current_date += datetime.timedelta(days=1)
        return city_list[int(select_city) -1], current_date

    def buy(self):
        buy_select = input("Which product do you want to buy? (1- %s) - C)ancel :" % str(len(Product.products)))
        if buy_select == 'C':
            return
        product_to_buy = Product.products[int(buy_select) - 1]
        qty_to_buy = input("How many {0} you wish to buy?: ".format(product_to_buy.name))
        cost_to_buy = product_to_buy.price * int(qty_to_buy)
        print(cost_to_buy)
        if cost_to_buy <= self.cash:
            self.cash -= cost_to_buy
            product_to_buy.shipqty += int(qty_to_buy)

    def sell(self):
        input("What do you want to sell? ")

    def visit_bank(self):
        input("How much you want to transfer? ")

    def display_products(self):
        i =1
        for product in Product.products:
            print("{0}){1}--{2}--{3}".format(i, product.name,product.price,product.shipqty))
            #print(str(i) + ")" + product.name + "--" + str(product.price) + "--" + str(product.shipqty))
            i += 1
            
    def start_up(self):
        game_running = True
        while game_running:
            # Display Main Game Interface
            os.system("cls")
            print(MENU_DIVIDER)
            print(GAME_TITLE)
            print(MENU_DIVIDER)
            #Using String Formatting: 3 different ways of formatting other than concatenation
            print("Firm Name: %s" % self.firm_name)
            print("Cash: {:,}".format(self.cash)) # Better way of formatting
            print(f"Debt: {self.debt}" ) # Another way of formatting in Python 3.6 or above, fstrings or string interpolation
            print("Cannons: %d"  % self.cannons)
            print("City: %s" % self.current_city.name)
            # http://strftime.org 
            print("Date: {:%B %d, %Y}".format(self.current_date))
            print(MENU_DIVIDER)
            print("------City Products------")
            self.display_products()
           
            has_bank_string = ""
            if self.current_city.has_bank == True:
                has_bank_string = "V)isit Bank,"
            print("Menu L)eave Port, B)uy, S)ell, T)ransfer Warehouse, %s Q)uit" % has_bank_string)
            menu_option = input("What is your option: ")
            if menu_option == "L":
                self.current_city, self.current_date = self.leave_port(City.cities, self.current_date)
            elif menu_option == "B":
                self.buy()
            elif menu_option == "S":
                self.sell()
            elif menu_option == "V" and self.current_city.has_bank == True:
                self.visit_bank()
            elif menu_option == "Q":
                #break
                game_running = False



