#!/usr/bin/python3

"""
3. Python is cool!
Start Execution of Flask web application on 0.0.0.0, port 5000
Similar to Task 2. Adds route /python
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


@app.route('/c/<text>', strict_slashes=False)
def show_c_text(text):
    """show the text after /c/"""

    return 'C %s' % text.replace("_", " ")


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_pythonis(text='is cool'):
    """show the text after /c/"""

    return 'Python %s' % text.replace("_", " ")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
