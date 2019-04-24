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

@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """returns whatever text is after the slash"""
    return "C {}".format(text.replace('_', ' '))

@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is(text="is cool"):
    """defaults to is cool, same as c_is_fun otherwise"""
    return "Python {}".format(text.replace('_', ' '))

if __name__ == "__main__":
    app.run()
