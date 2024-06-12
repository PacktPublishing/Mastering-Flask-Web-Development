from flask import Blueprint

complainant_bp = Blueprint('complainant_bp', __name__,
    template_folder='pages',
    static_folder='resources', static_url_path='static')


import modules.complainant.views.complainant