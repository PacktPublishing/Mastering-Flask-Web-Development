from flask import Blueprint

product_bp = Blueprint('product_bp', __name__)

import app.product.api.brand