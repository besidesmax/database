from sqlalchemy_utils import create_database, database_exists, drop_database
from engine import engine, engine_create
from classes import Base
from import_data import import_data_csv

# check if DB already exist
# If exist drop it and create a new one TODO: delete before finsh
if database_exists(engine):
    drop_database(engine)
    create_database(engine)
else:
    create_database(engine)

# creates all tables if not exist
Base.metadata.create_all(engine_create)

# imports all the data into the tables
import_data_csv()
