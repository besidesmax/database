from sqlalchemy import create_engine
from sqlalchemy_utils import create_database

# login-data for the Server TODO change with input or import form data at the end
hostname = "localhost"
username = "root"
# Achtung @ muss mit %40 und / muss mit %2F ersetzt werden
password = "!9PQ!X%40^1B5ChkwE"
port = "3306"
database = "database_university"

create_database("mysql+pymysql://" + username + ":" + password + "@" + hostname + ":" + port + "/" + database)


