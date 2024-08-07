#!/usr/bin/env python3
"""Basic Babel setup for the Flask App"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """The configuration object
    Usage:
    >>> app = Flask(__name__)
    >>> app.config.from_object(Config)
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Get hte locale from the request"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def home_page():
    """Render the Home page"""
    return render_template("2-index.html")
