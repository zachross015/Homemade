from urllib.parse import urlparse
from .websites import *
from .retrievers import HearstRetriever

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
    domain = domain.replace('www.', '')
    try:
        retriever = web_addresses[domain]
        return retriever.retrieve_meal(url)
    except KeyError as error:
        return 'There is either an error in the web address, or the domain has not been added yet.'
