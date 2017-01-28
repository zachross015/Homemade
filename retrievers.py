from abc import ABCMeta, abstractmethod
from bs4 import BeautifulSoup
from meal import Meal, Ingredient, Step
from multiprocessing import Process
import urllib2

'''
DataRetriever:
This class is abstract, so that each instance of the
class will be able to handle retrieval on its own. It provides a base for
objects to build off of
'''
class DataRetriever:
    # declare the class as abstract since python 2.7 is used
    __metaclass__ = ABCMeta
    # meal for data to be added to
    meal = Meal()

    # retrieve the data from the website
    @classmethod
    def retrieve_meal(cls, wa):
        response = urllib2.urlopen(wa)
        bs = BeautifulSoup(response.read(), 'html.parser')
        cls.parse_name(bs)
        cls.parse_est_time(bs)
        cls.parse_ingredients(bs)
        cls.parse_steps(bs)
        return cls.meal.format()

    # retrieve the name of the website
    @classmethod
    @abstractmethod
    def parse_name(cls, bs):
        pass

    # retrieve the estimated amount of time to make the meal
    @classmethod
    @abstractmethod
    def parse_est_time(cls, bs):
        pass

    # retrieve the ingredients
    @classmethod
    @abstractmethod
    def parse_ingredients(cls, bs):
        pass

    # retrieve the steps
    @classmethod
    @abstractmethod
    def parse_steps(cls, bs):
        pass

'''
ATTRRetriever:
Data retriever base class for sites that use attributes as a method of
storing and showing the data needed to obtain
'''
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

'''
HearstRetriever:
data retriever for any website under the Hearst Lifestyle and
Design Group brand. The sites include :
# Country Living
# Delish
'''
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
