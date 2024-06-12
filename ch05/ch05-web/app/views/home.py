from flask import current_app, jsonify, render_template, Response
from app import sock

@current_app.route('/ch05/web/index')
async def welcome():
    return render_template('index.html'), 200

