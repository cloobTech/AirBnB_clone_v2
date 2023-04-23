#!/usr/bin/python3
""" a script that starts a Flask web application:"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ return a strin"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ return a strin"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """return str + arg """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """ route has two options for the URL path."""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ function expects an int as param"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """ Return an html template"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
