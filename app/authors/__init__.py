from flask import Blueprint

authors_bp = Blueprint('authors', __name__)

from . import routes
