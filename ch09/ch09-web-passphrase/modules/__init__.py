from flask import Flask
import toml
from modules.models.config import init_db
from flask_session import Session 
from flask_talisman import Talisman
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_wtf.csrf import CSRFProtect

def create_app(config_file):
    app = Flask(__name__,template_folder='../modules/pages', static_folder='../modules/resources')   
    app.config.from_file(config_file, toml.load)
    app.config.from_prefixed_env()
    init_db()
    sess = Session(app)
    csrf = CSRFProtect(app)
    talisman = Talisman(app)
    csp = {
        'default-src': [
            '\'self\'',
            'https://code.jquery.com',
            'https://cdnjs.com',
            'https://cdn.jsdelivr.net',
        ]
    }
    hsts = {
        'max-age': 31536000,
        'includeSubDomains': True
    }
   
    talisman.force_https = True
    talisman.force_file_save = True
    talisman.x_xss_protection = True
    talisman.session_cookie_secure = True
    talisman.frame_options_allow_from = 'https://www.google.com'
    talisman.content_security_policy = csp
    talisman.strict_transport_security = hsts
    
    
    global limiter
    limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["30 per day", "5 per hour"],
    storage_uri="memory://",
      )
  
    with app.app_context():
        import modules.views.login
        import modules.views.admin
        import modules.views.vaccine
        import modules.views.patient
        import modules.views.doctor
        import modules.views.vaccination_center
        import modules.views.inventory
        import modules.views.vaccine_registration
        import modules.views.vaccine_card
    return app