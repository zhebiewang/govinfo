import govinfo.mysql_conn

# connection = MySQLdb.connect(user='root', passwd='root', db='govdb', host='localhost', charset="utf8", use_unicode=True)
# cursor = connection.cursor()
connection, cursor = open_database_connection()

cursor.execute ("SELECT VERSION()")
row = cursor.fetchone ()
print "server version:", row[0]

cursor.close()
connection.close()