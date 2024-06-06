from urllib.parse import quote

# Obtain database connection information from user input
hostname = input("Enter hostname (default is localhost): ") or "localhost"  # Default port is localhost
username = input("Enter username (default is root): ") or "root"  # Default port is root
password = input("Enter password: ") or "!9PQ!X@^1B5ChkwE"
password_url = quote(password, safe='')
port = input("Enter port (default is 3306): ") or "3306"  # Default port is 3306
database = "database_university"



