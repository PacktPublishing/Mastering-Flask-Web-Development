from flask import render_template, current_app, request, flash, redirect, url_for
from modules.repository.login import LoginRepository
from modules.models.config import db_session
from modules.models.db import Login
from flask_login import login_user, logout_user

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
async def login_valid_user():
    if request.method == 'GET':
        return render_template('login/authenticate.html'), 200
    username = request.form['username'].strip()
    password = request.form['password'].strip()
    async with db_session() as sess:
        async with sess.begin(): 
            repo = LoginRepository(sess)
            records = await repo.select_login_username_passwd(username, password)
            #login_rec = [rec.to_json() for rec in records]
            if(len(records) >= 1):
                login_user(records[0])
                return render_template('login/signup.html'), 200
            else:
                flash(f'Error adding { request.form["username"] }', 'error')
                return render_template('login/authenticate.html'), 200
            
@current_app.route("/logout")
async def logout():
    logout_user()
    return redirect(url_for('login_valid_user'))