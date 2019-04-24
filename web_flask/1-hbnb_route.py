#!/usr/bin/python3
"""starts a flask application"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_flask():
    """returns 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """returns HBNB"""
    return "HBNB"

if __name__ == "__main__":
    app.run()
