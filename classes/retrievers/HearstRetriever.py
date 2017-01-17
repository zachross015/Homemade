from attrretriever import ATTRRetriever
from classes import Step
# data retriever for any website under the Hearst Lifestyle and
# Design Group brand. The sites include :
# Country Living
# Delish
class HearstRetriever(ATTRRetriever):
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

    # retrieve the steps
    @classmethod
    def parse_steps(cls, bs):
        steps = bs.find(attrs={cls.attr_type():cls.steps_attr()}).findAll('li')
        for step in steps:
            s = Step(step.getText())
            cls.meal.steps.append(s)
