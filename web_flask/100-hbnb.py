#!/usr/bin/python3

"""
ABnB with places
Start Execution of Flask web application on 0.0.0.0, port 5000
"""

from models import storage
from models import State, Amenity, Place
from flask import Flask
from flask import render_template
app = Flask('web_flask')


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Show html page for /hbnb"""

    all_states = storage.all(State).values()
    all_amenities = storage.all(Amenity).values()
    all_places = storage.all(Place).values()

    return render_template('100-hbnb.html',
                           states=all_states,
                           amenities=all_amenities,
                           places=all_places)


@app.teardown_appcontext
def teardown_storage(response_or_exc):
    """Remove the current SQLAlchemy Session"""

    if storage is not None:
        storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
