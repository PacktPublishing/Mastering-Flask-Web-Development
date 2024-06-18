from flask import Flask
import toml
from modules.models.config import init_db
from modules.security.oauth2_config import PasswordGrant, query_client, save_token
from celery_config import celery_init_app

from authlib.integrations.flask_oauth2 import AuthorizationServer
from authlib.integrations.flask_oauth2 import ResourceProtector

require_oauth = ResourceProtector()
oauth_server = AuthorizationServer()

def create_app(config_file):
    app = Flask(__name__,template_folder='../modules/pages', static_folder='../modules/resources')   
    app.config.from_file(config_file, toml.load)
    app.config.from_prefixed_env()
  
    init_db()
    oauth_server.init_app(app, query_client=query_client, save_token=save_token)
    oauth_server.register_grant(PasswordGrant)
    
    celery_app = celery_init_app(app)
    
    with app.app_context():
        
        import modules.views.admin
        import modules.views.vaccine
        import modules.views.patient
        import modules.views.doctor
        import modules.views.login
    return app, celery_app