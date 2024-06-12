from flask import render_template, current_app

@current_app.route('/index', methods =['GET'])
def index():
    return render_template('index.html'), 200

@current_app.route('/menu', methods =['GET'])
def menu():
    return render_template('menu.html'), 200