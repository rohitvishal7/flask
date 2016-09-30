import MySQLdb as mdb

con = mdb.connect('localhost', 'root', 'root', 'test')

with con:

    cur = con.cursor(mdb.cursors.DictCursor)
    cur.execute("SELECT * FROM Writers LIMIT 4")

    itmes = cur.fetchall()

    for key in itmes:
        print key["Id"], key["Name"]