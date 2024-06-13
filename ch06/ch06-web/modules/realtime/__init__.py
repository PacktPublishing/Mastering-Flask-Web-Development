from flask import Blueprint

rt_bp = Blueprint("rt_bp", __name__, template_folder="pages", static_folder="resources", 
                       static_url_path="static")


import modules.realtime.views.realtime_sse_plots
import modules.realtime.views.realtime_ws_plots