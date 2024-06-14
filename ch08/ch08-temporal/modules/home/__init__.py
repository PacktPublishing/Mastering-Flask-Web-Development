
from flask import Blueprint
from temporalio.client import Client
from flask import jsonify, current_app

home_bp = Blueprint('home_bp', __name__,
    template_folder='pages',
    static_folder='resources', static_url_path='static')

def get_client() -> Client:
    return current_app.temporal_client

import modules.home.api.index
