from flask import Blueprint

external_bp = Blueprint("external_bp", __name__, template_folder="pages", static_folder="resources", 
                       static_url_path="static", url_prefix="/ch06")


import modules.external.views.computation_julia