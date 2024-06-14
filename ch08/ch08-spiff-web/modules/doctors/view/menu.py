from flask import Flask, render_template
from modules.doctors import doc_bp


@doc_bp.route('/menu/doc')
async def show_menu():
    return render_template("doc_dashboard.html")