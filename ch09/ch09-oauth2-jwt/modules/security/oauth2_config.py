from modules.services.login_task import get_user_task_wrapper
from modules.services.client_task import get_client_task_wrapper
from modules.services.token_task import add_token_task_wrapper, get_token_task_wrapper
from modules.models.db import Client, Token
from json import loads, dumps
from authlib.oauth2.rfc6750 import BearerTokenValidator
from authlib.integrations.flask_oauth2.requests import FlaskOAuth2Request
from authlib.jose import JsonWebKey
from authlib.oauth2.rfc7523 import JWTBearerGrant, JWTBearerTokenValidator
import os

class MyJWTBearerGrant(JWTBearerGrant):
    def resolve_issuer_client(self, issuer):
        task = get_client_task_wrapper.apply_async(args=[issuer])
        client:Client = task.get()
      

    def resolve_client_key(self, client, headers, payload):
        private_key = os.getcwd() + "\\key.pem"
        with open(private_key, mode='rb') as private_file:
            key_data = private_file.read()
            key = JsonWebKey.import_key(key_data, {'kty': 'RSA'})
        return key

    def authenticate_user(self, subject):
        result = get_user_task_wrapper.apply_async([subject, ])
        login = result.get()
        return login
    
      
class MyJWTBearerTokenValidator(JWTBearerTokenValidator):
    def get_jwks(self):
        return None
    
class MyBearerTokenValidator(BearerTokenValidator):
    def authenticate_token(self, token_string):
         task = get_token_task_wrapper.apply_async(args=[token_string])
         token:Token = task.get()
         if token is not None:
            return token    
        
def query_client(client_id):
    task = get_client_task_wrapper.apply_async(args=[client_id])
    client:Client = task.get()
    return client

def save_token(token_data, request:FlaskOAuth2Request):
    if request.user:
        user_id = request.user.user_id
    else:
        user_id = request.client.user_id
    
    token_dict = dict()
    token_dict['client_id'] = request.client.client_id
    token_dict['user_id'] = user_id
    token_dict['issued_at'] = request.client.client_id_issued_at
    token_dict['access_token_revoked_at'] = 0
    token_dict['refresh_token_revoked_at'] = 0
    token_dict['scope'] = request.client.client_metadata["scope"]
    token_dict.update(token_data)
    token_str = dumps(token_dict)
    task = add_token_task_wrapper.apply_async(args=[token_str])
    result = task.get()


