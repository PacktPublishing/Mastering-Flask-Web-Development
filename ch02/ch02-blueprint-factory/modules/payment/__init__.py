from flask import Blueprint
import modules
import modules.model.db

payment_bp = Blueprint('payment_bp', __name__,
    template_folder='pages',
    static_folder='resources', static_url_path='static')


import modules.payment.views.payment
