from classes.retrievers import ATTRRetriever
# data retriever for the website AllRecipes.com
class AllRecipes(ATTRRetriever):
    @classmethod
    def attr_type(cls):
        return 'class'
    @classmethod
    def name_attr(cls):
        return 'recipe-summary__h1'
    @classmethod
    def est_time_attr(cls):
        return 'ready-in-time'
    @classmethod
    def ingredients_attr(cls):
        return 'recipe-ingred_txt'
    @classmethod
    def steps_attr(cls):
        return 'recipe-directions__list--item'
