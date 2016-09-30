import sqlite3 as sql

def getConnection():
    return sql.connect("test.db")