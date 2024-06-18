from flask import render_template, current_app, request, flash, session, redirect
from modules.repository.vaccination_center import VacCenterRepository
from modules.models.db import VacCenter
from modules.models.config import db_session


@current_app.route('/vaccenter/add', methods = ['GET', 'POST'])
async def add_vaccenter():
    if not session.get("user"):
        return redirect('/login/auth')
    if request.method == "GET":
        return render_template('vaccine/add_vaccine_center.html'), 200
    async with db_session() as sess:
          async with sess.begin(): 
            repo = VacCenterRepository(sess)
            vaccenter_details = {
                "vaccenterid": request.form['vaccenterid'],
                "centername": request.form['centername'],
                "telephone": request.form['telephone'],
                "address": request.form['address'],
                "city": request.form['city'],
                "province": request.form['province'],
                "region": request.form['region']
            }
            vaccenter = VacCenter(**vaccenter_details)
            result = await repo.insert_vaccenter(vaccenter)
            print(result)
            if result == False:
                flash(f'Error adding new vaccination center profile.', 'error')
            else:
                flash(f'Successully added vaccination center { request.form["vaccenterid"] }.', 'success')
    return render_template('vaccine/add_vaccine_center.html'), 200

@current_app.route('/vaccenter/del', methods = ['GET', 'POST'])
async def delete_vaccenter():
    if request.method == "GET":
        return render_template('vaccine/del_vaccine_center.html'), 200