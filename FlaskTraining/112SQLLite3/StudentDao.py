import sqlite3 as sql

class StudentDao:
    def __init__(self, connection):
        self.connection = connection

    def addStudent(self, std):
        try:
            with self.connection as con:
                cur = con.cursor()

                cur.execute("INSERT INTO students (name,addr,city,pin)VALUES(?, ?, ?, ?)",
                            (std.name, std.address, std.city, std.pincode))

                con.commit()
                msg = "Record successfully added"

        except Exception as e:
            con.rollback()
            msg = "error in insert operation", e

        finally:
            con.close()
        return msg

    def getListOfStudent(self):
        con = self.connection
        con.row_factory = sql.Row

        cur = con.cursor()
        cur.execute("select * from students")

        rows = cur.fetchall();
        return rows
