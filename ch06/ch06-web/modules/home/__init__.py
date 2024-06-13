from flask import Blueprint

home_bp = Blueprint("home_bp", __name__, template_folder="pages", static_folder="resources", 
                       static_url_path="static")


from modules.home.views.index import home