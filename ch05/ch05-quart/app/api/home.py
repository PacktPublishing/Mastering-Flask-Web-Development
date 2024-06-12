from quart import jsonify, render_template
  
async def home():
    return jsonify(message='hello')

async def welcome():
    return await render_template('index.html'), 200