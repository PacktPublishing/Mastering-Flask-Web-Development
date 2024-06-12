import requests
from flask import current_app, render_template, request
from simplejson import dumps

@current_app.route('/client/order/add', methods = ['GET', 'POST'])
def add_order():
    if request.method == 'POST':
        order_dict = request.form.to_dict(flat=True)
        order_add_api = "http://localhost:5000/order/add"
        response:requests.Response = requests.post(order_add_api, json=order_dict)
    customers_list_api = "http://localhost:5000/customer/list/all"
    employees_list_api = "http://localhost:5000/employee/list/all"
    resp_customers:requests.Response = requests.get(customers_list_api)
    resp_employees:requests.Response = requests.get(employees_list_api)
    
    return render_template('add_order.html', customers=resp_customers.json(), employees=resp_employees.json())