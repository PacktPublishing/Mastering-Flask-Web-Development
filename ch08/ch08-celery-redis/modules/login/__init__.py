
from flask import Blueprint

login_bp = Blueprint('login_bp', __name__,
    template_folder='pages',
    static_folder='resources', static_url_path='static')



import modules.login.api.login