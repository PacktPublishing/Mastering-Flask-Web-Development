from flask import render_template, current_app, request
from modules.repository.login import LoginRepository
from modules.models.config import db_session
from flask_login import login_required

@current_app.route('/patient/profile/add', methods = ['GET', 'POST'])
@login_required
async def add_patient_profile():
    
    if request.method == 'GET':
        async with db_session() as sess:
          async with sess.begin(): 
            repo = LoginRepository(sess)
            records = await repo.select_all_patient()
            patient_rec = [rec.to_json() for rec in records]
            return render_template('patient/add_patient_profile.html', patients=patient_rec), 200
    else:
        username = request.form['username']
        if not username == 'None': 
           return render_template('login/authenticate.html'), 200
        else:
            async with db_session() as sess:
                async with sess.begin(): 
                    repo = LoginRepository(sess)
                    records = await repo.select_all_patient()
                    patient_rec = [rec.to_json() for rec in records]
                    return render_template('patient/add_patient_profile.html', patient=patient_rec), 200


@current_app.route('/patient/profile/delete/<int:id>', methods = ['GET', 'POST'])
@login_required
async def del_patient_profile_id(id:int):
    return render_template('patient/del_patient_profile.html'), 200


@current_app.route('/patient/profile/delete/<string:username>', methods = ['GET', 'POST'])
@login_required
async def del_patient_profile_username(username:str):
    return render_template('patient/del_patient_profile.html'), 200