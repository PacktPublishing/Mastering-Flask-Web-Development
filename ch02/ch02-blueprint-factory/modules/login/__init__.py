from flask import Blueprint

import modules.model.db


login_bp = Blueprint('login_bp', __name__,
    template_folder='pages',
    static_folder='resources', static_url_path='static')


import modules.login.views.login
import modules.login.views.admin
import modules.login.views.customer

