'''
This class is abstract, so that each instance of the
class will be able to handle retrieval on its own. It provides a base for
objects to build off of
'''
from abc import ABCMeta, abstractmethod
from bs4 import BeautifulSoup
from meal import Meal
from multiprocessing import Process
import urllib2
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
