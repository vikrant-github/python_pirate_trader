import random
from product import Product

# City Class
class City(object):
    cities = []
    # Constructor
    def __init__(self, name, has_warehouse, has_bank, has_moneylender):
        self.name = name
        self.has_warehouse = has_warehouse
        self.has_bank = has_bank
        self.has_moneylender = has_moneylender
        self.create_city_products()
        #self.price = random.randint(self.minprice, self.maxprice)
    @classmethod
    def create_cities(cls):
        cls.cities.append(City("Hong Kong", True, True, True))
        cls.cities.append(City("Shanghai", False, False, False))
        cls.cities.append(City("London", False, False, False))
    def create_city_products(self):
        self.city_products = []
        for product in Product.products:
            self.city_products.append(CityProduct(self,product))

class CityProduct(object):
    def __init__(self, city, product):
        self.city = city
        self.product = product
        self.generate_random_price()
    def generate_random_price(self):
        self.price = random.randint(self.product.minprice, self.product.maxprice)

 