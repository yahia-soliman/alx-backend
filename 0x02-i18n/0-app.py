#!/usr/bin/env python3
"""Basic Flask App demo"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home_page():
    """Render the Home page"""
    return render_template("0-index.html")
