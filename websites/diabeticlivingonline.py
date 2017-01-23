from classes.retrievers import ATTRRetriever
# data retriever for diabeticlivingonline
class DiabeticLivingOnline(ATTRRetriever):
    @classmethod
    def attr_type(cls):
        return 'itemprop'
    @classmethod
    def name_attr(cls):
        return 'page-title'
    @classmethod
    def est_time_attr(cls):
        return 'prepTime'
    @classmethod
    def ingredients_attr(cls):
        return 'ingredients'
    @classmethod
    def steps_attr(cls):
        return 'recipeInstructions'

    # retrieve the name of the website
    @classmethod
    def parse_name(cls, bs):
        name = bs.find(attrs={'id':cls.name_attr()}).getText()
        cls.meal.name = name

    @classmethod
    def parse_est_time(cls, bs):
        time = bs.find(attrs={'class':cls.est_time_attr()}).getText()
        cls.meal.est_time = time
