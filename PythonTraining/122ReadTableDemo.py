import MySQLdb as mdb

con = mdb.connect('localhost', 'root', 'root', 'test');

with con: 

    cur = con.cursor()
    cur.execute("SELECT * FROM Writers")

    rows = cur.fetchall()

    for row in rows:
        print row