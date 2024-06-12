from flask import render_template
from modules.home import home_bp

@home_bp.route("/index")
def home_index():
    return render_template('index.html'), 200