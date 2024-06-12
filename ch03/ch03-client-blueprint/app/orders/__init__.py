from flask import Blueprint

orders_client_bp = Blueprint('orders_client_bp', __name__,
    template_folder='pages',
    static_folder='resources', static_url_path='static')

import app.orders.views.orders_client