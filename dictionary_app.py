import os
import webapp2
import logging
from google.appengine.ext.webapp import template
from dictionary import Dictionary


class WebApplication(webapp2.RequestHandler):
    def get(self):

        logging.info("request.get:" + self.request.get('query'))
        query = self.request.get('query')

        if isinstance(query, str):
            query = unicode(query, 'utf-8')
        else:
            query = unicode(query)

        if query:
            logging.info("query: " + query)
        else:
            logging.info("query: None")

        test = self.request.get('radioGroup')
        logging.info("radioGroup: " + test)


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
                logging.info("WARNING: SearchOption missing!")
                results = Dictionary.find_word_excact(Dictionary(), query, 'nor')

            print "results: " + str(len(results))
        else:
            print "No results"

        numberOfHits = 0
        if results:
            numberOfHits = len(results)

        dictionary = Dictionary()

        template_values = {
            'dictionary': dictionary,
            'query': query,
            'searchOption': searchOption,
            'numberOfHits': numberOfHits,
            'results': results,
            }

        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))


app = webapp2.WSGIApplication([('/', WebApplication), ], debug=True)