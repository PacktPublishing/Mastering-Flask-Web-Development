import requests
from app.products import pizza_client_bp
from flask import  render_template


@pizza_client_bp.route('/client/pizza/list/all', methods = ['GET'])
def list_pizzas():
    pizza_list_url = 'http://localhost:5000/pizza/list/all'
    response = requests.get(pizza_list_url)
    return render_template('list_pizzas.html', pizzas=response.json())