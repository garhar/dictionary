# -*- coding: utf-8 -*-

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

dictionary = Dictionary()


def get_page():
    page = request.values.get('page')
    if not page:
        page = ""
    return page


def get_query():
    query = request.values.get('query')
    if not query:
        query = ""
    if query and isinstance(query, str):
        query = unicode(query, 'utf-8')
    elif query:
        query = unicode(query)
    return query


def get_mode():
    mode = request.values.get('mode')
    if not mode:
        mode = ""
    return mode


def get_option():
    option = request.values.get('option')
    if not option:
        option = ""
    return option


@app.route("/dictionary", methods=['GET'])
def dict_nor():

    results = None

    # Get page
    page = get_page()
    logger.info("Request page: " + page)

    # Get query
    query = get_query()
    logger.info("query: " + query)

    # Get mode
    mode = get_mode()
    logger.info("mode: " + mode)

    option = get_option()
    logger.info("option: " + option)

    logger.info("Start search...")
    if query != "" and mode and mode == "abbr":
        results = dictionary.find_abbriviations(option, query)
    else:
        results = dictionary.find_words(option, query, 'nor')

    logger.info("End search...")

    message = None
    if len(results) >= 200:
        message = "Listen er begrenset til 200 termer"
    elif results:
        message = "Fant " + str(len(results)) + " termer"
    else:
        message = "Fant ingen termer"

    return render_template('index.html', page=page, query=query,
                           mode=mode, option=option,
                           message=message, results=results)

@app.route("/dictionary/about", methods=['GET'])
def dict_about():
    return render_template('index.html', page='about')

@app.route("/dictionary/help", methods=['GET'])
def dict_help():
    return render_template('index.html', page='help')

@app.route("/dictionary/eng", methods=['GET'])
def dict_eng():
    return render_template('index.html', page='eng')

if __name__ == '__main__':
    if settings.is_debug():
        logger.info("DEBUG mode enabled")
        app.debug = True
    app.run(host='0.0.0.0', port=5000)
