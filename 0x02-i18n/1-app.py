#!/usr/bin/env python3
""" Basic Babel setup"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)

babel = Babel(app)


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route("/", strict_slashes=False)
def index():
    """ renders 1-index.html """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
