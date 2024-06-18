from asgiref.wsgi import WsgiToAsgi
from app import create_app
     
app = create_app('../config_dev.toml')

asgi_app = WsgiToAsgi(app)

# 