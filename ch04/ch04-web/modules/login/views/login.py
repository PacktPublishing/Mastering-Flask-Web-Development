from flask import render_template, request, session, redirect

from modules.login import login_bp
from main_cache import cache
from modules.login.forms.models import LoginForm, LoginAuthForm

from model.config import db_session
from model.db import Login
from modules.login.repository.login import LoginRepository

@login_bp.route('/login/add', methods = ['GET', 'POST']) 
def add_login():
    form:LoginForm = LoginForm()
    if request.method == 'GET':
        return render_template('login_add.html', form=form), 200
    if form.validate_on_submit():
        repo:LoginRepository = LoginRepository(db_session)
        login = Login(username=form.username.data, password=form.password.data, user_type=int(form.user_type.data[0]) )
        result = repo.insert(login)
        if result:
            records = repo.select_all()
            return render_template('login_list.html', records=records), 200
        else:
            return render_template('login_add.html', form=form), 500
    else:
        return render_template('login_add.html', form=form), 500
    

@login_bp.route('/login/auth', methods=['GET', 'POST']) 
def login_db_auth():
    authForm:LoginAuthForm = LoginAuthForm()
    if request.method == 'GET':
        return render_template('login.html', form=authForm) , 200
    if authForm.validate_on_submit():
        repo = LoginRepository(db_session)
        username = authForm.username.data
        password = authForm.password.data
        user:Login = repo.select_one_username(username)
        if user == None:

            return render_template('login.html', form=authForm) , 500
        elif not user.password == password:
    
            return render_template('login.html', form=authForm) , 500
        else:
            session['username'] = request.form['username']
            return redirect('/ch04/login/add')
    else:
        return render_template('login.html', form=authForm) , 500
            
@login_bp.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect('/ch04/login/auth')

