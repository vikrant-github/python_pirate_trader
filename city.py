
# City Class
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