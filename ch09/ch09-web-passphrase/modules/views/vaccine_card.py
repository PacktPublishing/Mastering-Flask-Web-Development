from flask import render_template, current_app, request, flash, session, redirect
from modules.repository.vaccine_card import VacCardRepository
from modules.repository.patient import PatientRepository
from modules.repository.doctor import DoctorRepository
from modules.repository.vaccine import VaccineRepository
from modules.models.db import VaccineCard
from modules.models.config import db_session
from datetime import datetime


@current_app.route('/vaccard/add', methods = ['GET', 'POST'])
async def add_vaccard():
    if not session.get("user"):
        return redirect('/login/auth')
    async with db_session() as sess:
        async with sess.begin(): 
          repo = VaccineRepository(sess)
          records = await repo.select_all_vaccine()
          vaccine_rec = [rec.to_json() for rec in records]
    async with db_session() as sess:
        async with sess.begin(): 
          repo = PatientRepository(sess)
          records = await repo.select_all_patient()
          patient_rec = [rec.to_json() for rec in records]
    async with db_session() as sess:
        async with sess.begin(): 
          repo = DoctorRepository(sess)
          records = await repo.select_all_doc()
          doc_rec = [rec.to_json() for rec in records]
    if request.method == "GET":
        return render_template('vaccine/add_vaccine_card.html', docs=doc_rec, patients=patient_rec, vaccines=vaccine_rec), 200
    async with db_session() as sess:
          async with sess.begin(): 
            repo = VacCardRepository(sess)
            card_details = {
                "cardid": request.form['cardid'],
                "patientid": request.form['patientid'],
                "docid": request.form['docid'],
                "vacid": request.form['vacid'],
                "date_vaccinated": 89.5
            }
            card = VaccineCard(**card_details)
            result = await repo.insert_vaccard(card)
            print(result)
            if result == False:
                flash(f'Error adding new vaccine card.', 'error')
            else:
                flash(f'Successully added vaccine card { request.form["cardid"] }.', 'success')
    return render_template('vaccine/add_vaccine_card.html', docs=doc_rec, patients=patient_rec, vaccines=vaccine_rec), 200