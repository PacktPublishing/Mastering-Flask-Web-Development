from flask import jsonify, current_app, request, session
from modules.repository.login import LoginRepository
from modules.models.config import db_session
from modules.models.db import Login
from werkzeug.security import generate_password_hash, gen_salt
from modules import oauth_server
from json import dumps
import time
from modules.services.client_task import add_client_task_wrapper
import os
from authlib.jose import JsonWebKey

@current_app.post('/login/signup')
async def login_signup():
     login_json = request.get_json()
     password = login_json["password"]
     passphrase = generate_password_hash(password)
     async with db_session() as sess:
          async with sess.begin(): 
            repo = LoginRepository(sess)
            login = Login(username=login_json["username"], user_id=login_json["username"], password=passphrase, role=login_json["role"])
            result = await repo.insert_login(login)
            if result == False:
                return jsonify(message="error in insert"), 201
            return jsonify(record=login_json), 200

@current_app.post('/login/client/add')
async def login_client_add():
    login_json = request.get_json()
    async with db_session() as sess:
        async with sess.begin(): 
            repo = LoginRepository(sess)
            records = await repo.select_login_username(login_json["username"])
            #login_rec = [rec.to_json() for rec in records]
            if(len(records) >= 1):
                #return render_template('login/signup.html'), 200
                session['id'] = login_json["username"]
    
    login_json = request.get_json()
    client_id = gen_salt(24)
    client_id_issued_at = int(time.time())
    client_id_expires_at =  int(time.time() + 60)
    private_key = os.getcwd() + "\\key.pem"
    with open(private_key, mode='rb') as private_file:
        key_data = private_file.read()
        key = JsonWebKey.import_key(key_data, {'kty': 'RSA'})
    client_details = {
        "client_id": client_id,
        "client_id_issued_at": client_id_issued_at,
        "client_id_expires_at": client_id_expires_at,
        "user_id": login_json["username"],
        "jwks": key.as_json()
    }
    client_metadata = {
        "client_name": login_json["client_name"],
        "grant_types": ["urn:ietf:params:oauth:grant-type:jwt-bearer"],
        "response_types": ["urn:ietf:params:oauth:grant-type:jwt-bearer"],
        "scope": "profile",
        "token_endpoint_auth_method": login_json["token_endpoint_auth_method"]
    }
    print(client_details)
    client_details_str = dumps(client_details)
    client_metadata_str = dumps(client_metadata)
    task = add_client_task_wrapper.apply_async(args=[client_details_str, client_metadata_str])
    result = task.get()
    print(result)
    return jsonify(message="created a client")

@current_app.route('/oauth/token', methods=['POST'])
async def issue_token():
    return oauth_server.create_token_response(request=request)


@current_app.get("/logout")
async def logout():
    return jsonify(record="logged-out user"), 201