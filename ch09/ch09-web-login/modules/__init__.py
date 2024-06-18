from flask import Flask
import toml
from modules.models.config import init_db
from flask_login import LoginManager
from celery_config import celery_init_app
from flask_session import Session

def create_app(config_file):
    app = Flask(__name__,template_folder='../modules/pages', static_folder='../modules/resources')   
    app.config.from_file(config_file, toml.load)
    app.config.from_prefixed_env()
    sess = Session(app)
    init_db()
    
    login_auth = LoginManager()
    login_auth.init_app(app)
    login_auth.session_protection = "strong"
    login_auth.login_view = "modules.views.login.login_valid_user"
    celery_app = celery_init_app(app)
    
    
    with app.app_context():
        
        import modules.views.admin
        import modules.views.vaccine
        import modules.views.patient
        import modules.views.doctor
        import modules.views.login
    return app, login_auth, celery_app