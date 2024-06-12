from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from model.config import Base
from main import app
import toml

app.config.from_file('config-dev.toml', toml.load)
db = SQLAlchemy(app, metadata=Base.metadata)
migrate = Migrate(app, db)




