from flask import Flask
import toml
from flask_cors import CORS, cross_origin
from modules_sub_flask.models.config import init_db


def create_app_sub(config_file):
    

    app = Flask(__name__)
    app.config.from_file(config_file, toml.load)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    
    init_db()
   

    with app.app_context():  
        from modules_sub_flask.api import home
        
        
    return app