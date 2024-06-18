from flask import render_template, current_app, request, flash, session, redirect, make_response
from markupsafe import escape
from modules.repository.login import LoginRepository
from modules.repository.doctor import DoctorRepository
from modules.repository.vaccination_center import VacCenterRepository
from modules.models.db import Doctor
from modules.models.config import db_session
import gladiator as glv

def validate_form(form_data):

    field_validations = ( 
        ('docid', glv.required, glv.length_max(12)), 
        ('username', glv.required, glv.type_(str)), 
        ('firstname', glv.required, glv.length_max(50), glv.regex_('[a-zA-Z][a-zA-Z ]+')), 
        ('midname', glv.required, glv.length_max(50), glv.regex_('[a-zA-Z][a-zA-Z ]+')), 
        ('lastname', glv.required, glv.length_max(50), glv.regex_('[a-zA-Z][a-zA-Z ]+')), 
        ('age', glv.required,  glv.length_max(3)), 
        ('email', glv.required, glv.length_max(25), glv.format_email), 
        ('mobile', glv.required, glv.length_max(15)), 
        ('vaccenterid', glv.required, glv.type_(str)), 
        ('status', glv.required, glv.in_(['true', 'false'])), 
        ('gender', glv.required, glv.in_(['male', 'female'])), 
    ) 
    result = glv.validate(field_validations, form_data) 
    return bool(result)

@current_app.route('/doctor/profile/add', methods = ['GET', 'POST'])
async def add_doctor_profile():
    if not session.get("user"):
        return redirect('/login/auth')
    async with db_session() as sess:
          async with sess.begin(): 
            repo = LoginRepository(sess)
            records = await repo.select_all_doctor()
            doc_rec = [rec.to_json() for rec in records]
    async with db_session() as sess:
          async with sess.begin(): 
            repo = VacCenterRepository(sess)
            records = await repo.select_all_vaccenter()
            vaccenter_rec = [rec.to_json() for rec in records]
            
    if request.method == 'GET':
            return render_template('doctor/add_doctor_profile.html', doctors=doc_rec, vaccenters=vaccenter_rec), 200
    else:
        result = validate_form(request.form)
        if result == False:
            flash(f'Validation problem.', 'error')
            return render_template('doctor/add_doctor_profile.html', doctors=doc_rec, vaccenters=vaccenter_rec), 200
        username = request.form['username']
        if username == 'None': 
           flash(f'Error adding new doctor profile.', 'error')
           return render_template('doctor/add_doctor_profile.html', doctors=doc_rec, vaccenters=vaccenter_rec), 200
        else:
           async with db_session() as sess:
             async with sess.begin(): 
                repo = DoctorRepository(sess)
                doc_details = {
                     "docid": escape(request.form['docid'].strip()),
                     "username": escape(request.form['username'].strip()),
                     "firstname": escape(request.form['firstname'].strip()),
                     "midname": escape(request.form['midname'].strip()),
                     "lastname": escape(request.form['lastname'].strip()),
                     "age": int(escape(request.form['age'].strip())),
                     "gender": escape(request.form['gender'].strip()),
                     "email": escape(request.form['email'].strip()),
                     "mobile": escape(request.form['mobile'].strip()),
                     "status": bool(escape(request.form['status'].strip())),
                     "vaccenterid": escape(request.form['vaccenterid'].strip())
                }
                doc = Doctor(**doc_details)
                result = await repo.insert_doctor(doc)
                if result == False:            
                    flash(f'Error adding new doctor profile.', 'error')
                else: 
                    flash(f'Successully added a user { request.form["username"] } profile.', 'success')
                return render_template('doctor/add_doctor_profile.html', doctors=doc_rec, vaccenters=vaccenter_rec), 200

@current_app.route('/doctor/profile/delete/<int:id>', methods = ['GET', 'POST'])
async def del_doctor_profile_id(id:int):
    if not session.get("user"):
        return redirect('/login/auth')
    async with db_session() as sess:
      async with sess.begin(): 
        repo = LoginRepository(sess)
        records = await repo.select_all_doctor()
        doc_rec = [rec.to_json() for rec in records]
    if request.method == 'GET':
        return render_template('admin/del_doctor_profile.html', doctors=doc_rec), 200
    else:
      username = request.form['username']
      async with db_session() as sess:
          async with sess.begin(): 
              repo = DoctorRepository(sess)
              result = await repo.delete_doc_username(username)
              if result == False:
                  flash(f'Error deleting doctor profile.', 'error')
              else:
                  flash(f'Successully deleted user { request.form["username"] } profile.', 'success')
      return render_template('admin/del_doctor_profile.html', doctors=doc_rec), 200

