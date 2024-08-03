#!/usr/bin/env python3
"""Demo using flask-babel
Mocking user login
"""
from flask import Flask, g, render_template, request
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
app.url_map.strict_slashes = False
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Get the current logged in User"""
    user_id = request.args.get("login_as")
    if user_id:
        return users.get(int(user_id))


@app.before_request
def before_request():
    """Attach the user object to the request"""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """Get hte locale from the request"""
    lang = request.args.get("locale")
    if lang in app.config["LANGUAGES"]:
        return lang
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def home_page():
    """Render the Home page"""
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
