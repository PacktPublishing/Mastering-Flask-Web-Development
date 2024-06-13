from flask import Blueprint

internal_bp = Blueprint("internal_bp", __name__, template_folder="pages", static_folder="resources", 
                       static_url_path="static", url_prefix="/ch06")

import modules.internal.views.compute_hpi