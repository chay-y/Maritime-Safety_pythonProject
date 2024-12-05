import sys
import mariadb

def mariaDbConnection(u, pw, h, p, d):
    try:
        conn = mariadb.connect(user = u, password = pw, host = h, port = p, database = d)
        print("DB Connection Success: {0}".format(h))
    except mariadb.Error as e:
        print("Error connecting to MariaDB Platform : {}".format(e))
        sys.exit(1)
 
    return conn
 
 
def mariaDbClose(c):
    try:
        c.close()
        print("DB Close Success")
    except mariadb.Error as e:
        print("Error closing from MariaDB Platform")
        sys.exit(1)