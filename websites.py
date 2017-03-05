from .retrievers import DataRetriever, ATTRRetriever
from .meal import Ingredient, Step

'''
AllRecipes:

'''
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

'''
DiabeticLivingOnline:

'''
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

'''
Kraft:

'''
# data retriever for the website AllRecipes.com
class Kraft(DataRetriever):

    # retrieve the name of the website
    @classmethod
    def parse_name(cls, bs):
        name = bs.find(attrs={'id':'khMainTitle'}).getText()
        cls.meal.name = name

    # retrieve the estimated amount of time to make the meal
    @classmethod
    def parse_est_time(cls, bs):
        time = bs.find(attrs={'itemprop':'cookTime'}).getText(separator=u' ')
        cls.meal.est_time = time

    # retrieve the ingredients
    @classmethod
    def parse_ingredients(cls, bs):
        ingreds = bs.findAll(attrs={'itemprop':'recipeIngredient'})
        for item in ingreds:
            ingredient = Ingredient(item.getText())
            cls.meal.ingredients.append(ingredient)

    # retrieve the steps
    @classmethod
    def parse_steps(cls, bs):
        steps = bs.find(attrs={'itemprop':'recipeInstructions'}).findAll('li')
        for step in steps:
            s = Step(step.getText())
            cls.meal.steps.append(s)
