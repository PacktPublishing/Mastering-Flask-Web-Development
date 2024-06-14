from flask import Flask
import toml
from modules.models.config import init_db

def create_app(config_file):
    app = Flask(__name__)
    app.config.from_file(config_file, toml.load)
    app.config.from_prefixed_env()
 
    init_db()
    with app.app_context():  
        
        from modules.login import login_bp
       
        app.register_blueprint(login_bp, url_prefix='/ch08')
       
    return app