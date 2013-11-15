import os
import webapp2
import logging
from google.appengine.ext.webapp import template
from dictionary import Dictionary
import datetime


dictionary = None


class WebApplication(webapp2.RequestHandler):
    def get(self):

        logging.info("Query: " + self.request.get('query'))
        log("Query: " + self.request.get('query'))
        query = self.request.get('query')

        if isinstance(query, str):
            query = unicode(query, 'utf-8')
        else:
            query = unicode(query)

        if query:
            log("query: " + query)
        else:
            log("query: None")

        log("Get dictionary...")

        dictionary = get_dictionary()

        log("Got dictionary")

        results = None
        searchOption = None
        if query:
            searchOption = self.request.get('search-option')
            logging.info("search-option: " + searchOption)
            if searchOption and searchOption == "exactWord":
                results = Dictionary.find_word_excact(Dictionary(), query, 'nor')
            elif searchOption and searchOption == "startsWith":
                results = Dictionary.find_word_startswith(Dictionary(), query, 'nor')
            elif searchOption and searchOption == "contains":
                results = Dictionary.find_word_contains(Dictionary(), query, 'nor')
            else:
                log("WARNING: SearchOption missing!")
                results = dictionary.find_word_excact(query, 'nor')

            print "results: " + str(len(results))
        else:
            print "No results"

        log("Search complete...")

        numberOfHits = "ingen"
        if results:
            numberOfHits = len(results)

        template_values = {
            'query': query,
            'searchOption': searchOption,
            'numberOfHits': numberOfHits,
            'results': results,
        }


        log("Response ready...")
        # path = os.path.join(os.path.dirname(__file__), 'index.html')
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))


class Help(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'help.html')
        self.response.out.write(template.render(path, None))

app = webapp2.WSGIApplication([('/', WebApplication),
                               ('/help', Help),])


def log(message):
    now = datetime.datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    logging.info(current_time + ": " + message)


def get_dictionary():
    app = webapp2.get_app()
    global dictionary
    dictionary = app.registry.get('dictionary')
    if not dictionary:
        dictionary = Dictionary()
        app.registry['dictionary'] = dictionary
        log('Initializeing dictionary...')
    else:
        log('Dictionary was already initiilized...')
    return dictionary