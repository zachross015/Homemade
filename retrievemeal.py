from websites import *
from retrievers import HearstRetriever
import traceback
from urlparse import urlparse

web_addresses = {
    'www.allrecipes.com'            : AllRecipes(),
    'www.countryliving.com'         : HearstRetriever(),
    'www.delish.com'                : HearstRetriever(),
    'www.diabeticlivingonline.com'  : DiabeticLivingOnline(),
    'www.kraftrecipes.com'          : Kraft(),

}

def retrieve_meal(url):
    parsed_uri = urlparse(url)
    domain = '{uri.netloc}'.format(uri=parsed_uri)
    try:
        r = web_addresses[domain]
        return r.retrieve_meal(url)
    except KeyError as error:
        return 'N/A'
