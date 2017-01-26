import websites
import classes.retrievers
from urlparse import urlparse


web_addresses = {
    'www.kraftrecipes.com'          : websites.Kraft(),
    'www.allrecipes.com'            : websites.AllRecipes(),
    'www.diabeticlivingonline.com'  : websites.DiabeticLivingOnline(),
    'www.countryliving.com'         : classes.retrievers.HearstRetriever(),
    'www.delish.com'                : classes.retrievers.HearstRetriever()

}

def retrieve_meal(url):
    parsed_uri = urlparse(url)
    domain = '{uri.netloc}'.format(uri=parsed_uri)
    retriever = web_addresses[domain]
    return retriever.retrieve_meal(url)
