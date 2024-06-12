
from flask import render_template, request, session, flash, redirect
from modules.model.db import  Login
from modules.model.config import db_session

from modules.login import login_bp
from modules.login.repository.login import LoginRepository

from main import  app

@login_bp.route('/login/add', methods=['GET', 'POST']) 
def add_login():
    if request.method == 'POST':
        app.logger.info('add_login POST view executed')
        login = Login(username=request.form['username'], password=request.form['password'], user_type=int(request.form['user_type']) )
        repo = LoginRepository(db_session)
        result = repo.insert(login)
        if result == True:
            flash('Successully added a user', 'success')
        else:
            flash(f'Error adding { request.form["username"] }', 'error')
        return render_template('login_add.html') , 200
    app.logger.info('add_login GET view executed')
    return render_template('login_add.html') , 200

@login_bp.route('/login/list', methods=['GET'])
def list_login():
     repo = LoginRepository(db_session)
     users = repo.select_all()
     session['sample'] = 'trial'
     flash('List of user credentials')
     return render_template('login_list.html', users=users) , 200

@login_bp.route('/login/auth', methods=['GET', 'POST']) 
def login_db_auth():
    if request.method == 'POST':
        app.logger.info('add_db_auth POST view executed')
        repo = LoginRepository(db_session)
        username = request.form['username'].strip()
        password = request.form['password'].strip()
        user:Login = repo.select_one_username(username)
        
        if user == None:
            flash(f'User account { request.form["username"] } does not exist.', 'error')
            return render_template('login.html') , 200
        elif not user.password == password:
            flash('Invalid password.', 'error')
            return render_template('login.html') , 200
        else:
            session['username'] = request.form['username']
            return redirect('/ch02/menu')
    app.logger.info('add_db_auth GET view executed')
    print("hello")
    return render_template('login.html') , 200
            
@login_bp.route('/logout', methods=['GET'])
def logout():
    session.clear()
    app.logger.info('logout view executed')
    return redirect('/ch02/login/auth')
 

