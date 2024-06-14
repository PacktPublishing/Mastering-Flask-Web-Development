from flask import Flask, render_template
from modules.admin import admin_bp


@admin_bp.route('/menu/admin')
async def show_menu():
    return render_template("admin_dashboard.html")