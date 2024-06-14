from flask import Flask, render_template
from modules.patient import patient_bp


@patient_bp.route('/menu/patient')
async def show_menu():
    return render_template("patient_dashboard.html")