from modules.home import home_bp

from flask import render_template


@home_bp.get("/main/home")
async def home():
    return render_template("index.html"), 200