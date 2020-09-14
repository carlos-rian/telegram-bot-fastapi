from os import getenv
from sqlalchemy import create_engine
from model import metadata


def init_app():
    """Create all tables"""
    engine = create_engine(getenv("SQL_DATABASE_URI"), echo=True)
    metadata.create_all(engine)
    # metadata.drop_all(engine)
