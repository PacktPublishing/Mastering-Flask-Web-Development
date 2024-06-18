from flask import render_template, current_app, request, flash
from modules.repository.login import LoginRepository
from modules.models.config import db_session

@current_app.route('/admin/profile/add', methods = ['GET', 'POST'])
async def add_admin_profile():
    if request.method == 'GET':
        async with db_session() as sess:
          async with sess.begin(): 
            repo = LoginRepository(sess)
            records = await repo.select_all_admin()
            admin_rec = [rec.to_json() for rec in records]
            return render_template('admin/add_admin_profile.html', admin=admin_rec), 200
    else:
        username = request.form['username']
        if not username == 'None': 
           return render_template('login/authenticate.html'), 200
        else:
           async with db_session() as sess:
             async with sess.begin(): 
                repo = LoginRepository(sess)
                records = await repo.select_all_admin()
                admin_rec = [rec.to_json() for rec in records]
                return render_template('admin/add_admin_profile.html', admin=admin_rec), 200
        
    

@current_app.route('/admin/profile/del/<int:id>', methods = ['GET', 'POST'])
async def del_admin_profile_id(id:int):
    return render_template('admin/del_admin_profile.html'), 200


@current_app.route('/admin/profile/del/<string:username>', methods = ['GET', 'POST'])
async def del_admin_profile_username(username:str):
    return render_template('admin/del_admin_profile.html'), 200