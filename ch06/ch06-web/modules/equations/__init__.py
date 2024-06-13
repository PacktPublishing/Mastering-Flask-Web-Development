from flask import Blueprint

eqn_bp = Blueprint("eqn_bp", __name__, template_folder="pages", static_folder="resources", 
                       static_url_path="static")


import modules.equations.views.index
import modules.equations.views.simple_solution
import modules.equations.views.plot_solution
import modules.equations.views.complex_solution