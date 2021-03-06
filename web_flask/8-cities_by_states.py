#!/usr/bin/python3
"""starts a flask app"""

from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def app_teardown(exc=None):
    """calls storage.close() on teardown"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def states_cities():
    """shows all states"""
    states = storage.all("State").values()
    return render_template(
        "8-cities_by_states.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
