from flask import g, render_template, request, session, flash, redirect, current_app


from app.model.db import db, Login
from app.repository.login import LoginRepository

@current_app.route('/login/add', methods=['GET', 'POST']) 
def add_login():
    if request.method == 'POST':
        current_app.logger.info('add_login POST view executed')
        login = Login(username=request.form['username'], password=request.form['password'], user_type=int(request.form['user_type']) )
        repo = LoginRepository(db)
        result = repo.insert(login)
        if result == True:
            flash('Successully added a user', 'success')
        else:
            flash(f'Error adding { request.form["username"] }', 'error')
        return render_template('login/login_add.html') , 200
    current_app.logger.info('add_login GET view executed')
    return render_template('login/login_add.html') , 200

@current_app.route('/login/list', methods=['GET'])
def list_login():
     repo = LoginRepository(g.get('db', db))
     users = repo.select_all()
     session['sample'] = 'trial'
     flash('List of user credentials')
     return render_template('login/login_list.html', users=users) , 200

@current_app.route('/login/auth', methods=['GET', 'POST']) 
def login_db_auth():
   
        if request.method == 'POST':
            current_app.logger.info('add_db_auth POST view executed')
            repo = LoginRepository(db)
            username = request.form['username'].strip()
            password = request.form['password'].strip()
            user:Login = repo.select_one_username(username)
            if user == None:
                flash(f'User account { request.form["username"] } does not exist.', 'error')
                return render_template('login/login.html') , 200
            elif not user.password == password:
                flash('Invalid password.', 'error')
                return render_template('login/login.html') , 200
            else:
                session['username'] = request.form['username']
                return redirect('/menu')
        current_app.logger.info('add_db_auth GET view executed')
        return render_template('login/login.html') , 200
   
@current_app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    current_app.logger.info('logout view executed')
    return redirect('/login/auth')
    
 

