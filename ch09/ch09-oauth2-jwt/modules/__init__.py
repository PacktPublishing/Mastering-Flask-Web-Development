from flask import Flask
import toml
from modules.models.config import init_db
from modules.security.oauth2_config import MyJWTBearerGrant, query_client, save_token, MyJWTBearerTokenValidator
from celery_config import celery_init_app
import os

from authlib.integrations.flask_oauth2 import AuthorizationServer
from authlib.integrations.flask_oauth2 import ResourceProtector

require_oauth = ResourceProtector()
oauth_server = AuthorizationServer()

def create_app(config_file):
    app = Flask(__name__,template_folder='../modules/pages', static_folder='../modules/resources')   
    app.config.from_file(config_file, toml.load)
    app.config.from_prefixed_env()
  
    init_db()
    oauth_server.init_app(app, save_token=save_token, query_client=query_client)
    oauth_server.register_grant(MyJWTBearerGrant)
    
    public_key = os.getcwd() + "\\cert.pem"
    with open(public_key, mode='rb') as public_file:
        key = public_file.read()
    
    require_oauth.register_token_validator(MyJWTBearerTokenValidator(public_key=key))
    celery_app = celery_init_app(app)
    
    with app.app_context():
        
        import modules.api.admin
        import modules.api.patient
        import modules.api.doctor
        import modules.api.login
    return app, celery_app