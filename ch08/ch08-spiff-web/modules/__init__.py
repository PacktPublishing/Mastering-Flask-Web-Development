from flask import Flask
import toml
from modules.models.config import init_db


def create_app(config_file):
    app = Flask(__name__)
    app.config.from_file(config_file, toml.load)
    init_db()
    with app.app_context():  
        from modules.doctors import doc_bp
        from modules.home import home_bp
        from modules.login import login_bp
        from modules.admin import admin_bp
        from modules.payment import payment_bp
       
        from modules.patient import patient_bp
        app.register_blueprint(home_bp, url_prefix='/ch08')
        app.register_blueprint(login_bp, url_prefix='/ch08')
        app.register_blueprint(admin_bp, url_prefix='/ch08')
        app.register_blueprint(doc_bp, url_prefix='/ch08')
        app.register_blueprint(patient_bp, url_prefix='/ch08')
        app.register_blueprint(payment_bp, url_prefix='/ch08')
    return app