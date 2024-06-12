from flask import jsonify, current_app

@current_app.get('/ch05/index')
async def index():
   return jsonify(message='Welcome to an Online Voting System.')