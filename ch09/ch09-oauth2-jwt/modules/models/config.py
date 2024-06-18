from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_scoped_session
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import NullPool

from asyncio import current_task

DB_URL = "postgresql+asyncpg://postgres:admin2255@localhost:5433/vrms_oauth2_jwt"
engine = create_async_engine(DB_URL, future=True, echo=True, pool_pre_ping=True, poolclass=NullPool)
db_session = async_scoped_session(sessionmaker(engine, expire_on_commit=False, class_=AsyncSession), scopefunc=current_task)

Base = declarative_base()

def init_db():
    import modules.models.db
    
