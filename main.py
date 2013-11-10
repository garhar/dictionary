from flask import Flask
from flask import render_template

import logging
from bootstrap import bootstrap

# Test

VERSION = '0.0.1'
app = Flask(__name__)
app.secret_key = 'alfLKlyhjlKYo8iuyhIouyjlHu'

logger = logging.getLogger('velox')

@app.route("/main", methods=['GET'])
def main():
    return render_template('help.html', hello='Hello Main')

if __name__ == '__main__':
    bootstrap()
    app.run(host='0.0.0.0', port=5000)
