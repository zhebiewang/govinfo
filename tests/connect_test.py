
import MySQLdb


#Database connection
def open_database_connection():
    #connection = MySQLdb.connect(user='root', passwd='root', db='govdb', host='localhost', charset="utf8", use_unicode=True)
    connection = MySQLdb.connect(user='root', passwd='root', db='govdb', host='192.168.1.111', charset="utf8", use_unicode=True)
    cursor = connection.cursor()
    return connection, cursor

def close_database_connection(cursor, connection):
    cursor.close()
    connection.close()
    return


connection, cursor = open_database_connection()

cursor.execute ("SELECT VERSION()")
row = cursor.fetchone ()
print "server version:", row[0]

cursor.close()
connection.close()