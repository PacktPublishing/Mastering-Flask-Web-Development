from flask import Blueprint

pizza_client_bp = Blueprint('pizza_client_bp', __name__,
    template_folder='pages',
    static_folder='resources', static_url_path='static')

import app.products.views.pizza_client