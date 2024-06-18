from flask import render_template, current_app, request, flash, redirect, session
from modules.repository.vaccine import VaccineRepository
from modules.models.db import Vaccine
from modules.models.config import db_session

@current_app.route('/vaccine/add', methods = ['GET', 'POST'])
async def add_vaccine():
    if not session.get("user"):
        return redirect('/login/auth')
    if request.method == "GET":
        return render_template('vaccine/add_vaccine.html'), 200
    async with db_session() as sess:
          async with sess.begin(): 
            repo = VaccineRepository(sess)
            vaccine_details = {
                "vacid": request.form['vacid'],
                "vacname": request.form['vacname'],
                "vacdesc": request.form['vacdesc'],
                "qty": int(request.form['qty']),
                "price": float(request.form['price']),
                "status": bool(request.form['status'])
            }
            vaccine = Vaccine(**vaccine_details)
            result = await repo.insert_vaccine(vaccine)
            print(result)
            if result == False:
                flash(f'Error adding new vaccine.', 'error')
            else:
                flash(f'Successully added vaccine { request.form["vaccenterid"] }.', 'success')
    return render_template('vaccine/add_vaccine.html'), 200
        

@current_app.route('/vaccine/center/add', methods = ['GET', 'POST'])
async def add_vaccine_center():
    return render_template('vaccine/add_vaccine_center.html'), 200


@current_app.route('/vaccine/registration', methods = ['GET', 'POST'])
async def add_vaccine_registration():
    return render_template('vaccine/add_vaccine_registration.html'), 200

@current_app.route('/vaccine/inventory', methods = ['GET', 'POST'])
async def add_vaccine_inventory():
    return render_template('vaccine/add_vaccine_inventory.html'), 200

@current_app.route('/vaccination/card', methods = ['GET', 'POST'])
async def add_vaccination_card():
    return render_template('vaccine/add_vaccine_card.html'), 200