from app.home  import home_bp
from flask import render_template

@home_bp.route('/index', methods =['GET'])
def index():
    return render_template('index.html'), 200