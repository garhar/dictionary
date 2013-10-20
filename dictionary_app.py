import os
import webapp2
import json
from google.appengine.ext.webapp import template
from dictionary_service import Dictionary


class WebApplication(webapp2.RequestHandler):
    def get(self):
        results = Dictionary.find_nor_words(Dictionary(), 'base')
        print "results: " + str(len(results))

        template_values = {
            'message': 'Hello world!',
            'results': results,
            }

        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))


# class Search(webapp2.RequestHandler):
#     def get(self):
#
#         results = Dictionary.find_nor_words(Dictionary(), 'base')
#
#         template_values = {
#             'message': 'Hello world!',
#             'results': results,
#             }
#
#         path = os.path.join(os.path.dirname(__file__), 'templates/main.html')
#         self.response.out.write(template.render(path, template_values))


app = webapp2.WSGIApplication([('/', WebApplication), ], debug=True)

#app = webapp2.WSGIApplication([('/searc', Search), ], debug=True)

if __name__ == '__main__':
    #bootstrap()
    app.run(host='0.0.0.0', port=5000)