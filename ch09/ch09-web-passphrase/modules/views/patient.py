from flask import render_template, current_app, request, flash, session, redirect
from markupsafe import escape
from modules.repository.login import LoginRepository
from modules.repository.patient import PatientRepository
from modules.models.db import Patient
from modules.models.config import db_session
from datetime import datetime
import gladiator as glv

def validate_form(form_data):

    field_validations = ( 
        ('patientid', glv.required, glv.length_max(20)), 
        ('username', glv.required, glv.type_(str)), 
        ('firstname', glv.required, glv.length_max(50), glv.regex_('[a-zA-Z][a-zA-Z ]+')), 
        ('midname', glv.required, glv.length_max(50), glv.regex_('[a-zA-Z][a-zA-Z ]+')), 
        ('lastname', glv.required, glv.length_max(50), glv.regex_('[a-zA-Z][a-zA-Z ]+')), 
        ('age', glv.required,  glv.length_max(3)), 
        ('email', glv.required, glv.length_max(25), glv.format_email), 
        ('mobile', glv.required, glv.length_max(15)), 
        ('address', glv.required, glv.length_max(100)), 
        ('birthday', glv.required, glv.regex_('^(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$')), 
        ('gender', glv.required, glv.in_(['male', 'female'])), 
    ) 
    result = glv.validate(field_validations, form_data) 
    return bool(result)

@current_app.route('/patient/profile/add', methods = ['GET', 'POST'])
async def add_patient_profile():
    if not session.get("user"):
        return redirect('/login/auth')
    async with db_session() as sess:
          async with sess.begin(): 
            repo = LoginRepository(sess)
            records = await repo.select_all_patient()
            patient_rec = [rec.to_json() for rec in records]
    if request.method == 'GET':
           return render_template('patient/add_patient_profile.html', patients=patient_rec), 200
    else:
        print("birthday", request.form['birthday'])
        result = validate_form(request.form)
        if result == False:
            flash(f'Validation problem.', 'error')
            return render_template('patient/add_patient_profile.html', patients=patient_rec), 200
        username = request.form['username']
        if username == 'None': 
           flash(f'Error adding new patient profile.', 'error')
           return render_template('patient/add_patient_profile.html', patients=patient_rec), 200
        else:
           async with db_session() as sess:
             async with sess.begin(): 
                repo = PatientRepository(sess)
                
                patient_details = {
                     "patientid": escape(request.form['patientid'].strip()),
                     "username": escape(request.form['username'].strip()),
                     "firstname": escape(request.form['firstname'].strip()),
                     "midname": escape(request.form['midname'].strip()),
                     "lastname": escape(request.form['lastname'].strip()),
                     "birthday": escape(request.form['birthday'].strip()),
                     "age": int(escape(request.form['age'].strip())),
                     "address": escape(request.form['address'].strip()),
                     "email": escape(request.form['email'].strip()),
                     "mobile": escape(request.form['mobile'].strip()),
                     "gender": escape(request.form['gender'].strip())
                }
                patient = Patient(**patient_details)
                result = await repo.insert_patient(patient)
                if result == False:            
                    flash(f'Error adding new patient profile.', 'error')
                else: 
                    flash(f"Successully added patient { request.form['username'] }'s profile.", 'success')
           return render_template('patient/add_patient_profile.html', patients=patient_rec), 200

