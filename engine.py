from sqlalchemy import create_engine
from config import hostname, username, port, database, password_url

# engine for sqlalchemy operations
engine_create = \
    create_engine("mysql+pymysql://" + username + ":" + password_url + "@" + hostname + ":" + port + "/" + database)
# engine for sqlalchemy_utils operations
engine = ("mysql+pymysql://" + username + ":" + password_url + "@" + hostname + ":" + port + "/" + database)
