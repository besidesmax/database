from sqlalchemy_utils import create_database, database_exists
from engine import engine, engine_create
from classes import Base

# check if DB already exist
# If not create a new one
if not database_exists(engine):
    create_database(engine)

# creates all tables if not exist
Base.metadata.create_all(engine_create)
