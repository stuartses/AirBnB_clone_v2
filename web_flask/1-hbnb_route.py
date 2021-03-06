#!/usr/bin/python3

"""
1. HBNB
Start Execution of Flask web application on 0.0.0.0, port 5000
With the routes '/' and '/hnbn'
"""

from flask import Flask
app = Flask('web_flask')


@app.route('/', strict_slashes=False)
def index():
    """Creates index page"""

    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Creates hbnb page"""

    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
