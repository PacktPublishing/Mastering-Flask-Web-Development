from flask import Blueprint

complaint_bp = Blueprint('complaint_bp', __name__,
    template_folder='pages',
    static_folder='resources', static_url_path='static')