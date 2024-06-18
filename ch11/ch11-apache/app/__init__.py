from flask import Flask
import toml


def create_app(config_file):
    app = Flask(__name__)
    app.config.from_file(config_file, toml.load)
   
    with app.app_context():  
        from app.users import users_bp
        from app.product import product_bp
        from app.login import login_bp
        
        app.register_blueprint(product_bp, url_prefix='/ch11')
        app.register_blueprint(users_bp, url_prefix='/ch11')
        app.register_blueprint(login_bp, url_prefix='/ch11')
        
        
    return app