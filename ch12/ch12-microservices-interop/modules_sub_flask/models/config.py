from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

DB_URL = "postgresql://postgres:admin2255@localhost:5433/olms_feedbacks"

engine = create_engine(DB_URL)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()

def init_db():
    import modules_sub_flask.models.db