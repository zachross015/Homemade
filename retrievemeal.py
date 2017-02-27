from websites import *
from retrievers import HearstRetriever
import traceback
from urllib.parse import urlparse

web_addresses = {
    'allrecipes.com'            : AllRecipes(),
    'countryliving.com'         : HearstRetriever(),
    'delish.com'                : HearstRetriever(),
    'diabeticlivingonline.com'  : DiabeticLivingOnline(),
    'kraftrecipes.com'          : Kraft(),

}

def retrieve_meal(url):
    parsed_uri = urlparse(url)
    domain = '{uri.netloc}'.format(uri=parsed_uri)
    print(parsed_uri)
    try:
        r = web_addresses[domain]
        return r.retrieve_meal(url)
    except KeyError as error:
        try:
            r = web_addresses['www.'+domain]
            return r.retrieve_meal(url)
        except KeyError as error:
            return 'There is either a web address, or the domain has not been added yet.'
