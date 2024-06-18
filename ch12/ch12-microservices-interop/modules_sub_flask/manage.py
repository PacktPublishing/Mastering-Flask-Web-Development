from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


from modules_sub_flask.models.config import Base
from modules_sub_flask import create_app_sub
import toml

app_sub = create_app_sub('config_sub_dev.toml')

db = SQLAlchemy(app_sub, metadata=Base.metadata)
migrate = Migrate(app_sub, db, render_as_batch=True)




