from flask import Blueprint
from jinja2 import FileSystemLoader



upload_bp = Blueprint("upload_bp", __name__, template_folder="pages", static_folder="resources", 
                       static_url_path="static")

import modules.upload.views.visualization
import modules.upload.views.analysis






