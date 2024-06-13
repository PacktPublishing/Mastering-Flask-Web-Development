from modules.equations import eqn_bp

from flask import render_template


@eqn_bp.get("/eqns/home")
async def home():
    return render_template("index.html"), 200