from flask import request, jsonify, current_app


@current_app.get("/index")
def home():
    return jsonify(message="sub_flask")