import pandas as pd
from urllib.parse import quote

confid_default = pd.read_csv("confid_default.csv", dtype=str)



# Obtain database connection information from user input
def get_hostname():
    hostname = input(f'Enter hostname (default is: {confid_default.loc[0,"hostname"]})') or confid_default.loc[0, "hostname"]
    confid_default.loc[0, "hostname"] = hostname
    return confid_default


def get_port():
    port = input(f'Enter port (default is: {confid_default.loc[0,"port"]})') or confid_default.loc[0, "port"]  # Default port is 3306
    confid_default.loc[0, "port"] = port
    return confid_default


def get_username():
    username = input(f'Enter username (default is: {confid_default.loc[0,"username"]})') or confid_default.loc[0, "username"]  # Default port is root
    confid_default.loc[0, "username"] = username
    return confid_default


def get_password():
    password = input(f'Enter password (default is: {confid_default.loc[0,"password"]})') or  confid_default.loc[0, "password"]
    confid_default.loc[0, "password"] = password
    return confid_default



hostname = get_hostname().loc[0, "hostname"]
port = get_port().loc[0, "port"]
username = get_username().loc[0, "username"]
password = get_password().loc[0, "password"]
password_url = quote(password, safe='')
database = "database_university"

confid_default.to_csv("confid_default.csv")