#!/usr/bin/python3

"""
0. Hello Flask!
Start Execution of Flask web application on 0.0.0.0, port 5000
"""

from flask import Flask
app = Flask('web_flask')


@app.route('/', strict_slashes=False)
def index():
    """Creates index page"""

    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
