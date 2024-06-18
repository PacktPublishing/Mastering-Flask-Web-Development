from flask import Flask
import toml

from app.models.config import database
from peewee_async import Manager



def create_app(config_file):
    
    app = Flask(__name__)
    app.config.from_file(config_file, toml.load)
 
    global conn_mgr
    conn_mgr = Manager(database)  
    database.set_allow_sync(False)
  

    with app.app_context():  
        from app.login import login_bp
        from app.users import users_bp
        from app.product import product_bp
        
        app.register_blueprint(product_bp, url_prefix='/ch11')
        app.register_blueprint(users_bp, url_prefix='/ch11')
        app.register_blueprint(login_bp, url_prefix='/ch11')
        
        
    return app