from flask import render_template, current_app, request, flash, redirect, session
from modules.repository.vaccine_registration import VacRegistrationRepository
from modules.repository.vaccine import VaccineRepository
from modules.repository.admin import AdminRepository
from modules.models.db import VacRegistration
from modules.models.config import db_session
from datetime import datetime

@current_app.route('/vacregistration/add', methods = ['GET', 'POST'])
async def add_vacregistration():
    if not session.get("user"):
        return redirect('/login/auth')
    async with db_session() as sess:
        async with sess.begin(): 
          repo = VaccineRepository(sess)
          records = await repo.select_all_vaccine()
          vaccine_rec = [rec.to_json() for rec in records]
    async with db_session() as sess:
        async with sess.begin(): 
          repo = AdminRepository(sess)
          records = await repo.select_all_admin()
          admin_rec = [rec.to_json() for rec in records]
    if request.method == "GET":
        return render_template('vaccine/add_vaccine_registration.html', admins=admin_rec, vaccines=vaccine_rec), 200
    async with db_session() as sess:
          async with sess.begin(): 
            repo = VacRegistrationRepository(sess)
            registration_details = {
                "vacid": request.form['vacid'],
                "regcode": request.form['regcode'],
                "adminid": request.form['adminid'],
                "date_registration": datetime.strptime(request.form['date_registration'], '%Y-%m-%d').date()
            }
            inventory = VacRegistration(**registration_details)
            result = await repo.insert_vacreg(inventory)
            print(result)
            if result == False:
                flash(f'Error adding new vaccine registration.', 'error')
            else:
                flash(f'Successully added vaccine registration { request.form["regcode"] }.', 'success')
    return render_template('vaccine/add_vaccine_registration.html', admins=admin_rec, vaccines=vaccine_rec), 200


