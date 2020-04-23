#!/usr/bin/python3

"""
ABnB filters
Start Execution of Flask web application on 0.0.0.0, port 5000
"""

from models import storage
from models import State, Amenity
from flask import Flask
from flask import render_template
app = Flask('web_flask')


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Show html page for /hbnb_filters"""

    all_states = storage.all(State).values()
    all_amenities = storage.all(Amenity).values()

    return render_template('10-hbnb_filters.html',
                           states=all_states,
                           amenities=all_amenities
    )


@app.teardown_appcontext
def teardown_storage(response_or_exc):
    """Remove the current SQLAlchemy Session"""

    if storage is not None:
        storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
