#!/usr/bin/env python3
"""
Get locale from request
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Config class
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(login_as):
    """returns a user dictionary or None if the ID cannot be found or if
    login_as was not passed"""
    return users.get(int(login_as), None) if login_as else None


@app.before_request
def before_request():
    """find a user if any, and set it as a global on flask.g.user"""
    g.user = get_user(request.args.get("login_as"))


@babel.localeselector
def get_locale():
    """
    determine the best match with our supported languages.
    """
    locale = request.args.get("locale")
    if locale:
        return locale
    user = request.args.get("login_as")
    if user:
        lang = users.get(int(user)).get("locale")
        if lang in app.config["LANGUAGES"]:
            return lang
    headers = request.headers.get("locale")
    if headers:
        return headers
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """
    render 3-index.html
    """
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
