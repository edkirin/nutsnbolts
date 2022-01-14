from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from nuts.config import Config


SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{Config.db_user}:{Config.db_password}"
    f"@{Config.db_host}:{Config.db_port}/{Config.db_name}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()
