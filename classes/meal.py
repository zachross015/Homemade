from step import Step
from ingredient import Ingredient
from functions import remove_white_space, title

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
        self.__format_name()
        self.__format_time()
        self.__format_ingredients()
        self.__format_steps()
        self.formatted_data += "</meal>"
        return self.formatted_data

    # strips the name of excess white space and then makes every word capitalized
    # then appends to the formatted_data
    def __format_name(self):
        self.name = str(self.name)
        self.name = title(self.name)
        self.name = remove_white_space(self.name)
        self.formatted_data += "<name>" + self.name + "</name>"

    # strips excess white space and then formats it into a default time
    # then appends to the formatted_data
    # NOT FINISHED
    def __format_time(self):
        self.est_time = remove_white_space(self.est_time)
        self.est_time = self.__parse_time(self.est_time)
        self.formatted_data += "<est_time>" + self.est_time + "</est_time>"

    # formats all of the ingredients by calling their format function
    # then appends to the formatted_data
    def __format_ingredients(self):
        self.formatted_data += "<ingredients>"
        for ingred in self.ingredients:
            self.formatted_data += ingred.format()
        self.formatted_data += "</ingredients>"

    # formats all of the steps by calling their format function
    # then appends to the formatted_data
    def __format_steps(self):
        self.formatted_data += "<steps>"
        for step in self.steps:
            self.formatted_data += step.format()
        self.formatted_data += "</steps>"

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
        return "<hour>" + str(hour) + "</hour><minute>" + str(minute) + "</minute>"

    # time parser for hour:min (clock) formats
    def __p_t_clock(self, tokens):
        tokens = tokens[0].split(':')
        return "<hour>" + str(tokens[0]) + "</hour><minute>" + str(tokens[1]) + "</minute>"
