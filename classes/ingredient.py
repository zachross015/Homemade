from unit import Unit
from functions import remove_white_space

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
        q = "<quantity>" + str(self.quantity) + "</quantity>"
        u = "<unit>"  + str(self.unit.name) + "</unit>"
        n = "<name>"  + str(self.name) + "</name>"
        o = "<optional>"  + str(self.optional) + "</optional>"
        return "<ingredient>" + q + u + n + o + "</ingredient>"

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
