#!C:\Users\conra\AppData\Local\Programs\Python\Python38
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="ccharlesr",
    passwd="Haloreach98!",
    database="SupplyDB")

mycursor=mydb.cursor()

parts1 = "INSERT INTO SupplyDB.Parts(pid, pname, color)"+\
         "VALUES('P1', 'Mother board', 'Grey')"

mycursor.execute(parts1)

parts2 = "INSERT INTO SupplyDB.Parts(pid, pname, color)"+\
         "VALUES('P2', 'CPU-AMD', 'White')"

mycursor.execute(parts2)

parts3 = "INSERT INTO SupplyDB.Parts(pid, pname, color)"+\
         "VALUES('P3', 'Case', 'Grey')"

mycursor.execute(parts3)

parts4 = "INSERT INTO SupplyDB.Parts(pid, pname, color)"+\
         "VALUES('P4', 'Monitor', 'White')"

mycursor.execute(parts4)

parts5 = "INSERT INTO SupplyDB.Parts(pid, pname, color)"+\
         "VALUES('P5', 'Cable', 'Red')"

mycursor.execute(parts5)

mydb.commit()
