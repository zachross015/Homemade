'''
Data retriever base class for sites that use attributes as a method of
storing and showing the data needed to obtain
'''

from classes import DataRetriever, Ingredient, Step
from abc import ABCMeta, abstractmethod

class ATTRRetriever(DataRetriever):
    __metaclass__ = ABCMeta
    # type of attribute used (i.e. class, id, itemprop, etc.)
    @classmethod
    @abstractmethod
    def attr_type(cls):
        pass
    # attribute name for name
    @classmethod
    @abstractmethod
    def name_attr(cls):
        pass
    # attribute name for time
    @classmethod
    @abstractmethod
    def est_time_attr(cls):
        pass
    # attribute name for ingredients
    @classmethod
    @abstractmethod
    def ingredients_attr(cls):
        pass
    # attribute name for steps
    @classmethod
    @abstractmethod
    def steps_attr(cls):
        pass


    # retrieve the name of the website
    @classmethod
    def parse_name(cls, bs):
        name = bs.find(attrs={cls.attr_type(): cls.name_attr()}).getText()
        cls.meal.name = name

    # retrieve the estimated amount of time to make the meal
    @classmethod
    def parse_est_time(cls, bs):
        time = bs.find(attrs={cls.attr_type(): cls.est_time_attr()}).getText()
        cls.meal.est_time = time

    # retrieve the ingredients
    @classmethod
    def parse_ingredients(cls, bs):
        ingreds = bs.findAll(attrs={cls.attr_type():cls.ingredients_attr()})
        for item in ingreds:
            ingredient = Ingredient(item.getText())
            cls.meal.ingredients.append(ingredient)

    # retrieve the steps
    @classmethod
    def parse_steps(cls, bs):
        steps = bs.findAll(attrs={cls.attr_type():cls.steps_attr()})
        for step in steps:
            s = Step(step.getText())
            cls.meal.steps.append(s)
