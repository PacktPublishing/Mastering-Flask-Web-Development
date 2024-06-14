from flask import Blueprint


doc_bp = Blueprint("doc_bp", __name__)

import modules.doctors.api.doctor