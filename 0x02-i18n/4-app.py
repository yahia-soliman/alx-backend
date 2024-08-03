#!/usr/bin/env python3
"""Basic Babel setup for the Flask App"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


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
    lang = request.args.get("locale")
    if lang:
        return lang
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def home_page():
    """Render the Home page"""
    return render_template("4-index.html")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
