#!/usr/bin/python3

"""
0. Hello Flask!
Start Execution of Flask on 0.0.0.0, port 5000
"""

from web_flask import app


@app.route('/', strict_slashes=False)
def index():
    """Creates index page"""

    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
