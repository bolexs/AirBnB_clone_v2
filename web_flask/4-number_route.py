#!/usr/bin/python3
"""Adding a Number route"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    text = text.replace("_", " ")
    return f"C {text}"


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def is_it_a_number(n):
    return f"{(n)} is a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)