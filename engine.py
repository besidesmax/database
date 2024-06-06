from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

from config import hostname, username, port, database, password_url

# engine for sqlalchemy operations
engine_create = \
    create_engine("mysql+pymysql://" + username + ":" + password_url + "@" + hostname + ":" + port + "/" + database)
# engine for sqlalchemy_utils operations
engine = ("mysql+pymysql://" + username + ":" + password_url + "@" + hostname + ":" + port + "/" + database)


def test_database_connection(engine):
    try:
        # Attempt to connect to the database
        connection = engine.connect()
        connection.close()
        print("Database connection successful.")
    except OperationalError as e:
        raise ConnectionError(f"Failed to connect to the database. Error: {e}")
