from unit import Unit
import re

class Ingredient:
    # amount of ingredient to use
    quantity = 0
    # the measuring unit (tsp, tbsp)
    unit = Unit.NONE
    # name of the food
    name = ""
    # states whether or not the ingredient is optional
    optional = False

    def __init__(self, str):
        self.parse(str)

    # formats the ingredient into XML
    def format(self):
        q = "<quantity>" + str(self.quantity) + "</quantity>"
        u = "<unit>"  + str(self.unit) + "</unit>"
        n = "<name>"  + str(self.name) + "</name>"
        o = "<optional>"  + str(self.optional) + "</optional>"
        return "<ingredient>" + q + u + n + o + "</ingredient>"

    # parses the ingredient from the given string
    def parse(self, in_str):
        self.parse_quantity(in_str)
        self.parse_unit(in_str)
        self.parse_name(in_str)
        self.name = re.sub(r'[^\x00-\x7F]+',' ', in_str)

    def parse_quantity(self, in_str):
        pass

    def parse_unit(self, in_str):
        pass

    def parse_name(self, in_str):
        pass
