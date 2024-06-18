from flask import render_template, current_app, request, flash, session, redirect
from modules.repository.inventory import InventoryRepository
from modules.repository.vaccine import VaccineRepository
from modules.repository.vaccination_center import VacCenterRepository
from modules.models.db import Inventory
from modules.models.config import db_session
from datetime import datetime

@current_app.route('/inventory/add', methods = ['GET', 'POST'])
async def add_inventory():
    if not session.get("user"):
        return redirect('/login/auth')
    async with db_session() as sess:
        async with sess.begin(): 
          repo = VaccineRepository(sess)
          records = await repo.select_all_vaccine()
          vaccine_rec = [rec.to_json() for rec in records]
    async with db_session() as sess:
        async with sess.begin(): 
          repo = VacCenterRepository(sess)
          records = await repo.select_all_vaccenter()
          vcenter_rec = [rec.to_json() for rec in records]
    if request.method == "GET":
        return render_template('vaccine/add_vaccine_inventory.html', vcenters=vcenter_rec, vaccines=vaccine_rec), 200
    async with db_session() as sess:
          async with sess.begin(): 
            repo = InventoryRepository(sess)
            inventory_details = {
                "vacid": request.form['vacid'],
                "vaccenterid": request.form['vaccenterid'],
                "date_delivered": datetime.strptime(request.form['date_delivered'], '%Y-%m-%d').date()
            }
            inventory = Inventory(**inventory_details)
            result = await repo.insert_inventory(inventory)
            print(result)
            if result == False:
                flash(f'Error adding new vaccine inventory.', 'error')
            else:
                flash(f'Successully added vaccine inventory for vaccine { request.form["vacid"] }.', 'success')
    return render_template('vaccine/add_vaccine_inventory.html', vcenters=vcenter_rec, vaccines=vaccine_rec), 200