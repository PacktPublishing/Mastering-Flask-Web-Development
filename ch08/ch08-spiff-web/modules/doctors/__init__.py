from flask import Blueprint

doc_bp = Blueprint('doc_bp', __name__,
    template_folder='pages',
    static_folder='resources', static_url_path='static')

import modules.doctors.view.menu
import modules.doctors.view.appointment