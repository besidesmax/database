import pandas as pd
from urllib.parse import quote

config_default = pd.read_csv("config_default.csv", dtype=str)


# Obtain database connection information from user input
def get_hostname():
    hostname = (input(f'Enter hostname (default is: {config_default.loc[0, "hostname"]})')
                or config_default.loc[0, "hostname"])
    config_default.loc[0, "hostname"] = hostname
    return config_default


def get_port():
    port = (input(f'Enter port (default is: {config_default.loc[0, "port"]})')
            or config_default.loc[0, "port"])  # Default port is 3306
    config_default.loc[0, "port"] = port
    return config_default


def get_username():
    username = (input(f'Enter username (default is: {config_default.loc[0, "username"]})')
                or config_default.loc[0, "username"])  # Default port is root
    config_default.loc[0, "username"] = username
    return config_default


def get_password():
    password = (input(f'Enter password (default is: {config_default.loc[0, "password"]})')
                or config_default.loc[0, "password"])
    config_default.loc[0, "password"] = password
    return config_default


hostname = get_hostname().loc[0, "hostname"]
port = get_port().loc[0, "port"]
username = get_username().loc[0, "username"]
password = get_password().loc[0, "password"]
password_url = quote(password, safe='')
database = "database_university"

config_default.to_csv("config_default.csv")
