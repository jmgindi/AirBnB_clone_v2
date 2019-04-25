#!/usr/bin/python3
"""starts a flask app"""

from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def app_teardown(exc=None):
    """calls storage.close() on teardown"""
    storage.close()

@app.route("/states_list", strict_slashes=False)
def states_list():
    """shows all states"""
    states = [v for k, v in storage.all("State").items()]
    return render_template("7-states_list.html", states=states)
