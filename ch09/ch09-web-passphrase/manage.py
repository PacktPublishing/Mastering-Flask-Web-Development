from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


from modules.models.config import Base
from modules import create_app

app = create_app('../config_dev.toml')
db = SQLAlchemy(app, metadata=Base.metadata)
migrate = Migrate(app, db)





