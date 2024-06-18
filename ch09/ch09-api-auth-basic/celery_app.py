from modules import create_app

app, celery, auth = create_app('../config_dev.toml')
