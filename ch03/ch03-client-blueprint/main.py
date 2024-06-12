from flask import Flask, Response
import toml

app = Flask(__name__)
app.config.from_file("config_dev.toml", toml.load)

from app.home import home_bp
from app.products import pizza_client_bp
from app.orders import orders_client_bp

app.register_blueprint(home_bp, url_prefix='/ch03')
app.register_blueprint(pizza_client_bp, url_prefix='/ch03')
app.register_blueprint(orders_client_bp, url_prefix='/ch03')

@app.before_request
def before_check_api_server():
    print("started order API access")

@app.before_request   
def before_log_pizza_bp():
    print("started product API access")
    
@app.after_request
def after_check_api_server(resp:Response):
    print("processing orders")
    return resp

@app.after_request
def after_log_pizza_bp(resp:Response):
    print("processing pizza")
    return resp

app.before_request_funcs = {
    # blueprint name: [list_of_functions]
    'orders_client_bp': [before_check_api_server],
    'pizza_client_bp': [before_log_pizza_bp]
}

app.after_request_funcs = {
    # blueprint name: [list_of_functions]
    'orders_client_bp': [after_check_api_server],
    'pizza_client_bp': [after_log_pizza_bp]
}

if __name__ == '__main__':
     app.run(port=5002)
