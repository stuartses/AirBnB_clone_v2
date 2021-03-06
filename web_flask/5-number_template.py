#!/usr/bin/python3

"""
5. Number template
Start Execution of Flask web application on 0.0.0.0, port 5000
Add a template for /number_template/<n>
"""

from flask import Flask
from flask import render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def show_number(n):
    """show number /number/"""

    return '%s is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Show html page for /number_tamplate"""

    return render_template('5-number.html', number=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
