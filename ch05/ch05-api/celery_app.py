from app import create_app

app, celery = create_app('../config_dev.toml')
#celery = app.extensions["celery"]