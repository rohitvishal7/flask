import MySQLdb as mdb

con = mdb.connect('localhost', 'root', 'root', 'test')
    
with con:    

    cur = con.cursor()
        
    cur.execute("UPDATE Writers SET Name = %s WHERE Id = %s", 
        ("I am bad guy", "4"))        
    
    print "Number of rows updated:",  cur.rowcount