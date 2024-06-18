from flask import Flask
import toml
from modules.models.config import init_db
from celery_config import celery_init_app
from flask_httpauth import HTTPDigestAuth
from flask_session import Session 
from cryptography.fernet import Fernet


def create_app(config_file):
    app = Flask(__name__,template_folder='../modules/pages', static_folder='../modules/resources')   
    app.config.from_file(config_file, toml.load)
    app.config.from_prefixed_env()
    init_db()
    celery_app = celery_init_app(app)
    global auth
    auth = HTTPDigestAuth()
    sess = Session(app)
    
    with open("enc_key.txt", mode="w") as file:
         file.write(Fernet.generate_key().decode())
    
    with app.app_context():
        import modules.api.login
        import modules.api.admin
        import modules.api.doctor
        import modules.api.patient
        import modules.api.vaccine
    return app, celery_app, auth