from step import Step
from ingredient import Ingredient
import re

def title(s):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
            lambda mo: mo.group(0)[0].upper() +
            mo.group(0)[1:].lower(),
            s)

class Meal:
    # array for holding all of the ingredients to be used
    ingredients = []
    # array for holding all of the steps in the recipe
    steps = []
    # name of the meal being made
    name = ""
    # estimated time to cook
    est_time = ""
    # string to hold the formatted data
    formatted_data = ""

    # formats all parts of the xml and then puts them together
    def format(self):
        self.formatted_data = "<meal>"
        self.format_name()
        self.format_time()
        self.format_ingredients()
        self.format_steps()
        self.formatted_data += "</meal>"
        return self.formatted_data

    # strips the name of excess white space and then makes every word capitalized
    # then appends to the formatted_data
    def format_name(self):
        self.name = str(self.name)
        self.name = self.name.strip()
        self.name = title(self.name)
        self.name = re.sub(r'[^\x00-\x7F]+',' ', self.name)
        self.formatted_data += "<name>" + self.name + "</name>"

    def parse_time(self, t):
        return str(t)

    # strips excess white space and then formats it into a default time
    # then appends to the formatted_data
    # NOT FINISHED
    def format_time(self):
        self.est_time = parse_time(self.est_time)
        self.est_time = self.est_time.replace('\n', ' ')    #
        self.est_time = self.est_time.replace('\r', '')     # For getting rid of
        self.est_time = self.est_time.replace('\t', '')     # extra whitespaces
        self.est_time = self.est_time.strip()               #
        self.formatted_data += "<est_time>" + self.est_time + "</est_time>"

    # formats all of the ingredients by calling their format function
    # then appends to the formatted_data
    def format_ingredients(self):
        self.formatted_data += "<ingredients>"
        for ingred in self.ingredients:
            self.formatted_data += ingred.format()
        self.formatted_data += "</ingredients>"

    # formats all of the steps by calling their format function
    # then appends to the formatted_data
    def format_steps(self):
        self.formatted_data += "<steps>"
        for step in self.steps:
            self.formatted_data += step.format()
        self.formatted_data += "</steps>"
