from modules import create_app

app, login_auth, celery = create_app('../config_dev.toml')
