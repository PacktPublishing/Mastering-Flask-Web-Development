from flask import Blueprint
from flask_restful import Api



home_bp = Blueprint('home_bp', __name__)

from modules.home.api.index import Hello

api = Api(home_bp)
api.add_resource(Hello, '/index')

