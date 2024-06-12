from flask import render_template, request, current_app
from modules.model.db import Admin
from modules.login.repository.admin import AdminRepository
from modules.login.services.login import get_login_id
from exceptions.db import DuplicateRecordException
from modules.login import login_bp

from modules import db

@login_bp.route('/admin/add', methods = ['GET', 'POST'])
def add_admin():
    if request.method == 'POST':
        current_app.logger.info('add_admin POST view executed')
        repo = AdminRepository(db)
        admin = Admin(id=int(request.form['id']), firstname=request.form['firstname'],
                      middlename=request.form['middlename'], lastname=request.form['lastname'],
                      email=request.form['email'], mobile=request.form['mobile'])
        
        result = repo.insert(admin)
        if result == False:
            raise DuplicateRecordException()
        logins = get_login_id(1, db)
        return render_template('admin_details_form.html', logins=logins), 200 
    current_app.logger.info('add_admin GET view executed')
    logins = get_login_id(1, db)
    return render_template('admin_details_form.html', logins=logins), 200 