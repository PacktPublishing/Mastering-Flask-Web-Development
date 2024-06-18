from flask import render_template, current_app, request, flash
from markupsafe import escape

from modules.repository.admin import AdminRepository
from modules.repository.login import LoginRepository
from modules.models.db import Administrator
from modules.models.config import db_session
from flask_login import login_required
import gladiator as glv
from gladiator.core import ValidationResult

def validate_form(form_data):

    field_validations = ( 
        ('adminid', glv.required, glv.length_max(12)), 
        ('username', glv.required, glv.type_(str)), 
        ('firstname', glv.required, glv.length_max(50), glv.regex_('[a-zA-Z][a-zA-Z ]+')), 
        ('midname', glv.required, glv.length_max(50), glv.regex_('[a-zA-Z][a-zA-Z ]+')), 
        ('lastname', glv.required, glv.length_max(50), glv.regex_('[a-zA-Z][a-zA-Z ]+')), 
        ('email', glv.required, glv.length_max(25), glv.format_email), 
        ('mobile', glv.required, glv.length_max(15)), 
        ('position', glv.required,  glv.length_max(100)), 
        ('status', glv.required, glv.in_(['true', 'false'])), 
        ('gender', glv.required, glv.in_(['male', 'female'])), 
    ) 
    result:ValidationResult = glv.validate(field_validations, form_data) 
    return result.success

@current_app.route('/admin/profile/add', methods = ['GET', 'POST'])
async def add_admin_profile():
    
    async with db_session() as sess:
        async with sess.begin(): 
          repo = LoginRepository(sess)
          records = await repo.select_all_admin()
          admin_rec = [rec.to_json() for rec in records]
    if request.method == 'GET':
            return render_template('admin/add_admin_profile.html', admin=admin_rec), 200
    else:
        result = validate_form(request.form)
        if result == False:
            flash(f'Validation problem.', 'error')
            return render_template('admin/add_admin_profile.html', admin=admin_rec), 200
        username = request.form['username']
        if username == 'None': 
           flash(f'Error adding new admin profile.', 'error')
           return render_template('admin/add_admin_profile.html', admin=admin_rec), 200
        else:
           async with db_session() as sess:
             async with sess.begin(): 
                repo = AdminRepository(sess)
                admin_details = {
                     "adminid": escape(request.form['adminid'].strip()),
                     "username": escape(request.form['username'].strip()),
                     "firstname": escape(request.form['firstname'].strip()),
                     "midname": escape(request.form['midname'].strip()),
                     "lastname": escape(request.form['lastname'].strip()),
                     "email": escape(request.form['email'].strip()),
                     "mobile": escape(request.form['mobile'].strip()),
                     "position": escape(request.form['position'].strip()),
                     "status": bool(escape(request.form['status'].strip())),
                     "gender": escape(request.form['gender'].strip())
                }
                admin = Administrator(**admin_details)
                result = await repo.insert_admin(admin)   
                if result == False:            
                    flash(f'Error adding new admin profile.', 'error')
                else: 
                    flash(f'Successully added a user { request.form["username"] } profile.', 'success')
                return render_template('admin/add_admin_profile.html', admin=admin_rec), 200
        
@current_app.route('/admin/profile/del/<int:id>', methods = ['GET', 'POST'])
@login_required
async def del_admin_profile_id(id:int):
    return render_template('admin/del_admin_profile.html'), 200


@current_app.route('/admin/profile/del/<string:username>', methods = ['GET', 'POST'])
@login_required
async def del_admin_profile_username(username:str):
    return render_template('admin/del_admin_profile.html'), 200