
import MySQLdb as mdb

con = mdb.connect('localhost', 'root', 'root', 'test');

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM Writers")

    for i in range(cur.rowcount):
        
        row = cur.fetchone()
        print row[0], row[1]