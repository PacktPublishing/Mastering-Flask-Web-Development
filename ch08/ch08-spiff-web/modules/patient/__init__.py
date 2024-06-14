from flask import Blueprint

patient_bp = Blueprint('patient_bp', __name__,
    template_folder='pages',
    static_folder='resources', static_url_path='static')


import modules.patient.view.menu