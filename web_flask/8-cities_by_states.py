#!/usr/bin/python3

"""
Cities by states
Start Execution of Flask web application on 0.0.0.0, port 5000
"""

from models import storage
from models import State
from flask import Flask
from flask import render_template
app = Flask('web_flask')


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Show html page for /cities_by_states"""

    all_data = storage.all(State).values()

    return render_template('8-cities_by_states.html', data=all_data)


@app.teardown_appcontext
def teardown_storage(response_or_exc):
    """Remove the current SQLAlchemy Session"""

    if storage is not None:
        storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
