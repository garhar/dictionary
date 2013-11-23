from flask import Flask
from flask import render_template, request

from dictionary import Dictionary

import settings
import logging

VERSION = '0.0.1'
app = Flask(__name__)
app.secret_key = 'alfLKlyhjlKYo8iuyhIouyjlHu1'
app.jinja_env.globals['settings'] = settings
app.logger.addHandler(settings.vlh)
logger = logging.getLogger('dictionary')

@app.route("/dictionary", methods=['GET'])
def main():

    logger.error("test")
    query = request.values.get('query')
    if query and isinstance(query, str):
        query = unicode(query, 'utf-8')
    elif query:
        query = unicode(query)

    if query:
        logger.info("query: " + query)
    else:
        query = ""
        logger.info("query: None")

    logger.info("Get dictionary...")

    dictionary = Dictionary()

    logger.info("Got dictionary")

    results = None
    searchOption = None
    if query:
        searchOption = request.values.get('search-option')
        # logging.info("search-option: " + searchOption)
        if searchOption and searchOption == "exactWord":
            results = Dictionary.find_word_excact(Dictionary(), query, 'nor')
        elif searchOption and searchOption == "startsWith":
            results = Dictionary.find_word_startswith(Dictionary(),
                                                      query, 'nor')
        elif searchOption and searchOption == "contains":
            results = Dictionary.find_word_contains(Dictionary(), query, 'nor')
        else:
            logger.info("WARNING: SearchOption missing!")
            results = dictionary.find_word_excact(query, 'nor')

        print "results: " + str(len(results))
    else:
        print "No results"

    logger.info("Search complete...")

    numberOfHits = "ingen"
    if results:
        numberOfHits = len(results)

    return render_template('index.html', query=query,
                           searchOption=searchOption,
                           numberOfHits=numberOfHits, results=results)

if __name__ == '__main__':
    if settings.is_debug():
        logger.info("DEBUG mode enabled")
        app.debug = True
    app.run(host='0.0.0.0', port=5000)
