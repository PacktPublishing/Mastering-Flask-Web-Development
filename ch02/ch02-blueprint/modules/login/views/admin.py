from flask import render_template, request
from modules.login import login_bp

from modules.login.repository.admin import AdminRepository
from modules.login.services.login import get_login_id
from main import  app
from modules.model.db import Admin
from modules.model.config import db_session
from exceptions.db import DuplicateRecordException

@login_bp.route('/admin/add', methods = ['GET', 'POST'])
def add_admin():
    if request.method == 'POST':
        app.logger.info('add_admin POST view executed')
        repo = AdminRepository(db_session)
        admin = Admin(id=int(request.form['id']), firstname=request.form['firstname'],
                      middlename=request.form['middlename'], lastname=request.form['lastname'],
                      email=request.form['email'], mobile=request.form['mobile'])
        
        result = repo.insert(admin)
        if result == False:
            raise DuplicateRecordException()
        logins = get_login_id(1, db_session)
        return render_template('admin_details_form.html', logins=logins), 200 
    app.logger.info('add_admin GET view executed')
    logins = get_login_id(1, db_session)
    return render_template('admin_details_form.html', logins=logins), 200 