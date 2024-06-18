from authlib.oauth2.rfc6749.grants import AuthorizationCodeGrant
from modules.services.login_task import get_user_task_wrapper
from modules.services.client_task import get_client_task_wrapper
from modules.services.token_task import add_token_task_wrapper, get_token_task_wrapper, get_token_refresh_task_wrapper
from modules.services.code_task import add_authcode_task_wrapper, get_authcode_task_wrapper
from modules.models.db import Client, Token
from json import loads, dumps
from authlib.oauth2.rfc6750 import BearerTokenValidator
from authlib.integrations.flask_oauth2.requests import FlaskOAuth2Request
from authlib.oauth2.rfc7009 import RevocationEndpoint as _RevocationEndpoint
import time


class MyAuthorizationCodeGrant(AuthorizationCodeGrant):
    TOKEN_ENDPOINT_AUTH_METHODS = [
        'client_secret_basic', 'client_secret_post' ]
    
    def save_authorization_code(self, code, request):
        code_challenge = request.data.get('code_challenge')
        code_challenge_method = request.data.get('code_challenge_method')
        auth_details_dict = {
            "code" : code,
            "client_id" : request.client.client_id,
            "redirect_uri" : request.redirect_uri,
            "scope": request.scope,
            "user_id":request.client.user_id,
            "code_challenge": code_challenge,
            "auth_time": int(time.time()),
            "code_challenge_method": code_challenge_method,
        }
        auth_details_str = dumps(auth_details_dict)
        authcode_result = add_authcode_task_wrapper.apply_async(args=[auth_details_str])
        result = authcode_result.get()
        authcode = get_authcode_task_wrapper.apply_async(args=[code, request.client.client_id])
        result = authcode.get()
        return result

    def query_authorization_code(self, code, client):
        authcode = get_authcode_task_wrapper.apply_async(args=[code, client.client_id])
        result = authcode.get()
        if result.code and not result.is_expired():
            return result

    def delete_authorization_code(self, authorization_code):
        authcode = get_authcode_task_wrapper.apply_async(args=[authorization_code.code])
        result = authcode.get()

    def authenticate_user(self, authorization_code):
        result = get_user_task_wrapper.apply_async(authorization_code.user_id)
        login = result.get()
        return login
    
    
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
    print(token_str)
    task = add_token_task_wrapper.apply_async(args=[token_str])
    result = task.get()
    print(result)


class RevocationEndpoint(_RevocationEndpoint):
	
    def query_token(self, token, token_type_hint, client):
        if not token:
            task = get_token_refresh_task_wrapper.apply_async(args=[token])
            token:Token = task.get()
            return token
        if token_type_hint == 'access_token':
            task = get_token_task_wrapper.apply_async(args=[token])
            token:Token = task.get()
            return token
        elif token_type_hint == 'refresh_token':
            task = get_token_refresh_task_wrapper.apply_async(args=[token])
            token:Token = task.get()
            return token
        # without token_type_hint
        else:
            task = get_token_task_wrapper.apply_async(args=[token])
            token:Token = task.get()
            return token
        
    def revoke_token(self, token:Token):
        token.access_token_revoked_at = int(time.time())
        token_dict = dict()
        token_dict['client_id'] = token.client_id
        token_dict['user_id'] = token.user_id
        token_dict['issued_at'] = token.issued_at
        token_dict['access_token_revoked_at'] = token.access_token_revoked_at
        token_dict['refresh_token_revoked_at'] = token.refresh_token_revoked_at
        token_dict['scope'] = token.scope
        token_str = dumps(token_dict)
        task = add_token_task_wrapper.apply_async(args=[token_str])
        result = task.get()