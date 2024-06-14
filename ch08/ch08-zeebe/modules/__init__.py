from flask import Flask
import toml
from celery_config import celery_init_app
from modules.doctors import doc_bp
from modules.models.config import init_db

def create_app(config_file):
    app = Flask(__name__)   
    app.config.from_file(config_file, toml.load)
    app.config.from_prefixed_env()
    celery_app = celery_init_app(app)
    init_db()
    with app.app_context():
        app.register_blueprint(doc_bp, url_prefix='/ch08')
       
    return app, celery_app