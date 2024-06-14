from modules.home import home_bp
from flask import jsonify

@home_bp.route('/index', methods = ['GET'])
async def index():
    return jsonify(message="working")