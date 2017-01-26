from classes import DataRetriever,Ingredient, Step
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
