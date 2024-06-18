from flask import render_template, current_app, request, flash, redirect, session
from modules.repository.login import LoginRepository
from modules.models.config import db_session
from modules.models.db import Login
from werkzeug.security import generate_password_hash, gen_salt
import time
from modules import oauth_server
from authlib.oauth2 import OAuth2Error
from json import loads, dumps
from modules.services.client_task import add_client_task_wrapper
from modules.security.oauth2_config import RevocationEndpoint

@current_app.route('/login/signup', methods=['GET', 'POST'])
async def view_signup():
    if request.method == 'GET':
        return render_template('login/signup.html'), 200
    username = request.form['username'].strip()
    password = request.form['password'].strip()
    passphrase = generate_password_hash(password)
    role = request.form['role'].strip()
    async with db_session() as sess:
        async with sess.begin(): 
            repo = LoginRepository(sess)
            login = Login(username=username, user_id=username, password=passphrase, role=int(role))
            result = await repo.insert_login(login)
            
            if result == True:
                flash('Successully added a user', 'success')
            else:
                flash(f'Error adding { request.form["username"] }', 'error')
            return render_template('login/signup.html'), 200

@current_app.route('/login/user', methods=['GET', 'POST'])
async def login_valid_user():
    if request.method == 'GET':
        return render_template('login/user.html'), 200
    username = request.form['username'].strip()
    password = request.form['password'].strip()
    async with db_session() as sess:
        async with sess.begin(): 
            repo = LoginRepository(sess)
            records = await repo.select_login_username(username)
            #login_rec = [rec.to_json() for rec in records]
            if(len(records) >= 1):
                #return render_template('login/signup.html'), 200
                session['id'] = username
                return redirect('/login/client/add')
            else:
                flash(f'Error adding { request.form["username"] }', 'error')
                return render_template('login/user.html'), 200

@current_app.route('/login/client/add', methods=['GET', 'POST'])
async def login_client_add():
    if 'id' in session:
        async with db_session() as sess:
            async with sess.begin(): 
                repo = LoginRepository(sess)
                login = await repo.select_login_username(session['id'])
    if not login[0]:
        return redirect('/login/user')
    if request.method == 'GET':
        return render_template('login/authenticate.html')
    
    client_id = gen_salt(24)
    client_id_issued_at = int(time.time())
    client_id_expires_at =  int(time.time() + 60)
    client_details = {
        "client_id": client_id,
        "client_id_issued_at": client_id_issued_at,
        "client_id_expires_at": client_id_expires_at,
        "user_id": login[0].username
    }
    client_metadata = {
        "client_name": request.form["client_name"],
        "grant_types": ["code"],
        "response_types": ["code"],
        "redirect_uris": ["https://authlib.org/"],
        "scope": "profile",
        "state": "xyz",
        "token_endpoint_auth_method": request.form["token_endpoint_auth_method"]
    }
    print(client_details)
    client_details_str = dumps(client_details)
    client_metadata_str = dumps(client_metadata)
    task = add_client_task_wrapper.apply_async(args=[client_details_str, client_metadata_str])
    result = task.get()
    print(result)
    return redirect('/oauth/authorize', code=302)

@current_app.route('/oauth/authorize', methods=['GET', 'POST'])
async def login_authorize():
    if 'id' in session:
        async with db_session() as sess:
            async with sess.begin(): 
                repo = LoginRepository(sess)
                login = await repo.select_login_username(session['id'])
   
    if not login[0]:
        return redirect('/login/user')
    if request.method == 'GET':
        try:
            print(login[0].username)
            grant = oauth_server.get_consent_grant(end_user=login[0])
            print(grant)
        except OAuth2Error as error:
            print(error)
            return error.error
        return render_template('login/authenticate_confirm.html', user=login[0], grant=grant)
    
    return oauth_server.create_authorization_response(request=request,grant_user=login[0])

@current_app.route('/oauth/redirect', methods=['GET'])
def redirect_uri():
    return render_template('login/user.html'), 200

@current_app.route('/token/revoke', methods=['POST'])
def revoke_token():
	return oauth_server.create_endpoint_response(RevocationEndpoint.ENDPOINT_NAME)
   
@current_app.route("/logout")
async def logout():
    return render_template('login/user.html'), 200