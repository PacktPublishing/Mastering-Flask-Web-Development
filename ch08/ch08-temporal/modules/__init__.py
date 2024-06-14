from flask import Flask
import toml
from modules.models.config import init_db
from celery_config import celery_init_app

def create_app(config_file):
    app = Flask(__name__)
    app.config.from_file(config_file, toml.load)
    app.config.from_prefixed_env()
    celery_app = celery_init_app(app)
    init_db()
    with app.app_context():  
        from modules.home import home_bp
        from modules.admin import admin_bp
        
        app.register_blueprint(home_bp, url_prefix='/ch08')
        app.register_blueprint(admin_bp, url_prefix='/ch08')
      
    return app, celery_app