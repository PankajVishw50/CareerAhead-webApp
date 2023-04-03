from flask import Blueprint
from ..model import Permission

main = Blueprint('main', __name__)

from . import views
