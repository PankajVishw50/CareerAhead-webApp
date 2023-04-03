from . import main
from flask import render_template, flash, session


@main.route("/")
def index():
    return render_template("main/index.html")
