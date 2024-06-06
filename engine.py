from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

# login-data for the Server TODO change with input or import form data at the end
hostname = "localhost"
username = "root"
# Achtung @ muss mit %40 und / muss mit %2F ersetzt werden
password = "!9PQ!X%40^1B5ChkwE"
port = "3306"
database = "database_university"

# TODO insert Test if Server exist and connection is possible
# engine for sqlalchemy operations
engine_create = \
    create_engine("mysql+pymysql://" + username + ":" + password + "@" + hostname + ":" + port + "/" + database)
# engine for sqlalchemy_utils operations
engine = ("mysql+pymysql://" + username + ":" + password + "@" + hostname + ":" + port + "/" + database)


def test_database_connection(engine):
    try:
        # Attempt to connect to the database
        connection = engine.connect()
        connection.close()
        print("Database connection successful.")
    except OperationalError as e:
        raise ConnectionError(f"Failed to connect to the database. Error: {e}")