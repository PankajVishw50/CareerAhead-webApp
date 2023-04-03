from flask import Blueprint

counsellor = Blueprint("counsellor", __name__)

from . import views
