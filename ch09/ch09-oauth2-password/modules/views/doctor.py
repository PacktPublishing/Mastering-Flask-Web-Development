from flask import render_template, current_app, request, flash
from modules.repository.login import LoginRepository
from modules.models.config import db_session
from modules import require_oauth

@current_app.route('/doctor/profile/add', methods = ['GET', 'POST'])
@require_oauth("user_admin")
async def add_doctor_profile():
    if request.method == 'GET':
        async with db_session() as sess:
          async with sess.begin(): 
            repo = LoginRepository(sess)
            records = await repo.select_all_doctor()
            doc_rec = [rec.to_json() for rec in records]
            return render_template('doctor/add_doctor_profile.html', docs=doc_rec), 200
    else:
        username = request.form['username']
        if not username == 'None': 
           return render_template('login/authenticate.html'), 200
        else:
           async with db_session() as sess:
              async with sess.begin(): 
                repo = LoginRepository(sess)
                records = await repo.select_all_doctor()
                doc_rec = [rec.to_json() for rec in records]
                return render_template('doctor/add_doctor_profile.html', doctors=doc_rec), 200


@current_app.route('/doctor/profile/delete/<int:id>', methods = ['GET', 'POST'])
async def del_doctor_profile_id(id:int):
    return render_template('doctor/del_doctor_profile.html'), 200


@current_app.route('/doctor/profile/delete/<string:username>', methods = ['GET', 'POST'])
async def del_doctor_profile_username(username:str):
    return render_template('doctor/del_doctor_profile.html'), 200