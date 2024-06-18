from flask import render_template, current_app, request, flash, session, redirect
from modules.repository.login import LoginRepository
from modules.models.config import db_session
from modules.models.db import Login
from modules import limiter

from sqlalchemy_utils.types.encrypted.encrypted_type import (
    AesEngine,
    AesGcmEngine,
    DatetimeHandler,
    FernetEngine,
    InvalidCiphertextError
)

@current_app.route('/login/signup', methods=['GET', 'POST'])
async def view_signup():
    if request.method == 'GET':
        return render_template('login/signup.html'), 200
    username = request.form['username'].strip()
    password = request.form['password'].strip()
    role = int(request.form['role'].strip())
    async with db_session() as sess:
        async with sess.begin(): 
            repo = LoginRepository(sess)
            login = Login(username=username, password=password, role=role)
            result = await repo.insert_login(login)
            if result == True:
                flash('Successully added a user', 'success')
            else:
                flash(f'Error adding { request.form["username"] }', 'error')
            return render_template('login/signup.html'), 200

@current_app.route('/login/auth', methods=['GET', 'POST'])
@limiter.limit("5 per minute")
async def login_user():
    if request.method == 'GET':
        return render_template('login/authenticate.html'), 200
    username = request.form['username'].strip()
    password = request.form['password'].strip()
    async with db_session() as sess:
        async with sess.begin(): 
            repo = LoginRepository(sess)
            records = await repo.select_login_username_passwd(username, password)
            login_rec = [rec.to_json() for rec in records]
            if(len(login_rec) >= 1):
                session["user"] = username
                return redirect('/login/signup')
            else:
                flash(f'Error adding { request.form["username"] }', 'error')
                return render_template('login/authenticate.html'), 200

@current_app.route('/logout', methods=['GET'])
async def logout():
    session["user"] = None
    return redirect('/login/auth')