from flask import Blueprint

bp = Blueprint('api', __name__)

from app.api import game
from app.api import lifeforms
