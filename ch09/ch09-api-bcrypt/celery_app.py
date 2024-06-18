from modules import create_app

app, celery = create_app('../config_dev.toml')
