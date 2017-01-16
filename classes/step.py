'''
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
        return "<step>" + self.description + "</step>"
