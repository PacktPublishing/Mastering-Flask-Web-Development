from flask import Flask
from flask_bootstrap import Bootstrap4
from main_cache import cache
from mail_config import mail
from flask_wtf import CSRFProtect

import toml

from model.config import init_db
from flask_session import Session 

init_db()

app = Flask(__name__, template_folder='pages', static_folder="resources")   
app.config.from_file('config-dev.toml', toml.load)
bootstrap = Bootstrap4(app)
sess = Session()
csrf = CSRFProtect(app)

cache.init_app(app)
sess.init_app(app)
mail.init_app(app)
    
from modules.home import home_bp
from modules.login import login_bp
from modules.admin import admin_bp
from modules.complainant import complainant_bp
from modules.complaint import complaint_bp
   
app.register_blueprint(home_bp, url_prefix='/ch04')
app.register_blueprint(login_bp, url_prefix='/ch04')
app.register_blueprint(admin_bp, url_prefix='/ch04')
app.register_blueprint(complainant_bp, url_prefix='/ch04')
app.register_blueprint(complaint_bp, url_prefix='/ch04')

cache.clear()

if __name__ == '__main__':
    app.run()

