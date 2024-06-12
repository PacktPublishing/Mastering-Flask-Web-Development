import requests
from flask import current_app, render_template


@current_app.route('/client/pizza/list/all', methods = ['GET'])
def list_pizzas():
    pizza_list_url = 'http://localhost:5000/pizza/list/all'
    response = requests.get(pizza_list_url)
    return render_template('list_pizzas.html', pizzas=response.json())