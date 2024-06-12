from modules.home  import home_bp
from flask import render_template

@home_bp.route('/index', methods =['GET'])
def index():
    return render_template('index.html'), 200

@home_bp.route('/menu', methods =['GET'])
def menu():
    return render_template('menu.html'), 200