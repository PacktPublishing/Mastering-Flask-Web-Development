from flask import Blueprint
import modules
import modules.model.db

order_bp = Blueprint('order_bp', __name__,
    template_folder='pages',
    static_folder='resources', static_url_path='static')

import modules.order.views.order

