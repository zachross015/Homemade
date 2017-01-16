from classes.retrievers import ATTRRetriever
# data retriever for the website AllRecipes.com
class CountryLiving(ATTRRetriever):
    @classmethod
    def attr_type(cls):
        return 'itemprop'
    @classmethod
    def name_attr(cls):
        return 'name'
    @classmethod
    def est_time_attr(cls):
        return 'totalTime'
    @classmethod
    def ingredients_attr(cls):
        return 'ingredients'
    @classmethod
    def steps_attr(cls):
        return 'recipeInstructions'
