from flask import Blueprint

users_bp = Blueprint('users_bp', __name__)

import app.users.api.admin
import app.users.api.customer