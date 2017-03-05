from enum import Enum
from .functions import remove_white_space, title

'''
Unit:

'''
class Unit(Enum):
    NONE    = 0       # No Units
    TSP     = 1       # Teaspoon
    TBSP    = 2       # Tablespoon
    FLOZ    = 3       # Fluid Ounce
    CUP     = 4       # Cup
    PINT    = 5       # Pint
    QUART   = 6       # Quart
    GAL     = 7       # Gallon
    ML      = 8       # Milliliter
    L       = 9       # Liter
    DL      = 10      # Deciliter
    IB      = 11      # Pound
    OZ      = 12      # Ounce
    MG      = 13      # Milligram
    G       = 14      # Gram
    KG      = 15      # Kilogram
    SMALL   = 16      # Small Size
    MEDIUM  = 17      # Medium Size
    LARGE   = 18      # Large Size

    @classmethod
    def get_unit(cls, str):
        str = str.lower()
        vals = {
            'tsp':          1,
            'tsp.':         1,
            'teaspoon':     1,
            'teaspoons':    1,
            'tbsp':         2,
            'tbsp.':        2,
            'tablespoon':   2,
            'tablespoons':  2,
            'fl. oz.':      3,
            'fl oz':        3,
            'floz':         3,
            'fluid ounce':  3,
            'fluid ounces': 3,
            'c':            4,
            'c.':           4,
            'cup':          4,
            'cups':         4,
            'pt':           5,
            'pt.':          5,
            'pint':         5,
            'pints':        5,
            'qt':           6,
            'qt.':          6,
            'quart':        6,
            'quarts':       6,
            'gal':          7,
            'gal.':         7,
            'gallon':       7,
            'gallons':      7,
            'ml':           8,
            'ml.':          8,
            'milliliter':   8,
            'milliliters':  8,
            'l':            9,
            'l.':           9,
            'liter':        9,
            'liters':       9,
            'dl':           10,
            'dl.':          10,
            'deciliter':    10,
            'deciliters':   10,
            'lb':           11,
            'lb.':          11,
            'pound':        11,
            'pounds':       11,
            'oz':           12,
            'oz.':          12,
            'ounce':        12,
            'ounces':       12,
            'mg':           13,
            'mg.':          13,
            'milligram':    13,
            'milligrams':   13,
            'g':            14,
            'g.':           14,
            'gram':         14,
            'grams':        14,
            'kg':           15,
            'kg.':          15,
            'kilogram':     15,
            'kilograms':    15,
            'small':        16,
            'medium':       17,
            'large':        18
        }
        if vals.get(str) != None:
            value = vals[str]
        else:
            value = 0
        return Unit(value)

'''
Ingredient:

'''
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
        self.__parse(str)

    # formats the ingredient into XML
    def format(self):
        q = "\"quantity\":" + str(self.quantity) + ","
        u = "\"unit\":\""  + str(self.unit.name) + "\","
        n = "\"name\":\""  + title(str(self.name)) + "\","
        o = "\"optional\":\""  + str(self.optional) + "\""
        return "{" + q + u + n + o + "}"

    # parses the ingredient from the given string
    def __parse(self, in_str):
        in_str = remove_white_space(in_str)
        tokens = in_str.split()
        self.__parse_quantity(tokens)
        self.__parse_unit(tokens)
        self.__parse_name(tokens)

    # parse the quantity by checking sequential values until the value is no
    # longer a number
    def __parse_quantity(self, tokens):
        i = 0
        value = ''
        while i < len(tokens):
            if tokens[i].isnumeric():      #  check if value is number
                value += tokens[i]
                i += 1
            elif tokens[i].find('/') != -1:   #  check if value is fraction
                #fraction tokens
                f_tokens = tokens[i].split('/')
                if len(f_tokens) > 1 and f_tokens[0].isnumeric() and f_tokens[1].isnumeric:
                    value += f_tokens[0] + '/' + f_tokens[1]
                i += 1
            else:
                break
        del tokens[:i]
        self.quantity = value


    def __parse_unit(self, tokens):
        if len(tokens) <= 1:
            self.unit = Unit.NONE
        else:
            if tokens[0] == '-':
                del tokens[:1]
            unit = Unit.get_unit(tokens[0])
            if unit != Unit.NONE:
                self.unit = unit
                del tokens[:1]
            else:
                unit = Unit.get_unit(tokens[0] + ' ' + tokens[1])
                if unit!= Unit.NONE:
                    self.unit = unit
                    del tokens[:2]
                else:
                    self.unit = Unit.NONE


    def __parse_name(self, tokens):
        self.name = ' '.join(tokens)

'''
Step:
This class will later be formatted so that it will parse the description and
find all instances of ingredients and quantities. It will highlight the
ingredients used in each step, or at least format them differently.
it will also format any time stated in each step.
'''
class Step:
    # string to hold the step
    description = ""

    def __init__(self, d):
        self.description = d

    def format(self):
        self.description = self.description.replace('\n', '')    #
        self.description = self.description.replace('\r', '')     # For getting rid of
        self.description = self.description.replace('\t', '')     # extra whitespaces
        self.description = self.description.strip()
        return "\"" + self.description + "\""

'''
Meal:

'''
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
        self.formatted_data = "{"
        self.__format_name()
        self.__format_time()
        self.__format_ingredients()
        self.__format_steps()
        self.formatted_data += "}"
        return self.formatted_data

    # strips the name of excess white space and then makes every word capitalized
    # then appends to the formatted_data
    def __format_name(self):
        if self.name != 'N/A':
            self.name = str(self.name)
            self.name = title(self.name)
            self.name = remove_white_space(self.name)
            self.formatted_data += "\"name\":\"" + self.name + "\","

    # strips excess white space and then formats it into a default time
    # then appends to the formatted_data
    # NOT FINISHED
    def __format_time(self):
        if self.est_time != 'N/A':
            self.est_time = remove_white_space(self.est_time)
            self.est_time = self.__parse_time(self.est_time)
            self.formatted_data += "\"est_time\":{" + self.est_time + "},"

    # formats all of the ingredients by calling their format function
    # then appends to the formatted_data
    def __format_ingredients(self):
        if self.ingredients != 'N/A':
            self.formatted_data += "\"ingredients\":["
            first = True
            for ingred in self.ingredients:
                if not first:
                    self.formatted_data += ','
                self.formatted_data += ingred.format()
                first = False
            self.formatted_data += "],"

    # formats all of the steps by calling their format function
    # then appends to the formatted_data
    def __format_steps(self):
        if self.steps != 'N/A':
            self.formatted_data += "\"steps\":["
            first = True
            for step in self.steps:
                if not first:
                    self.formatted_data += ','
                self.formatted_data += step.format()
                first = False
            self.formatted_data += "]"

    def __parse_time(self, t):
        t = str(t)
        tokens = t.split()
        # for x hour y min formats
        if len(tokens) > 1 and len(tokens) % 2 == 0:
            t = self.__p_t_hour_min(tokens)
        elif len(tokens) == 1 and tokens[0].find(':') != -1:
            t = self.__p_t_clock(tokens)
        return t

    # time parser for x hour y min formats
    def __p_t_hour_min(self, tokens):
        hour = 0
        minute = 0
        for i in range(0,len(tokens), 2):
            if tokens[i+1][0] == 'h':
                hour = tokens[i]
            elif tokens[i+1][0] == 'm':
                minute = tokens[i]
        return "\"hour\":" + str(hour) + ",\"minute\":" + str(minute)

    # time parser for hour:min (clock) formats
    def __p_t_clock(self, tokens):
        tokens = tokens[0].split(':')
        return "\"hour\":" + str(tokens[0]) + ",\"minute\":" + str(tokens[1])
