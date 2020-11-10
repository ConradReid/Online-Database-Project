#!C:\Users\conra\AppData\Local\Programs\Python\Python38
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="ccharlesr",
    passwd="Haloreach98!",
    database="SupplyDB")

mycursor=mydb.cursor()

suppliers1 = "INSERT INTO SupplyDB.Suppliers(sid, sname, address) VALUES(111, 'John Smith', '1 Elizabeth Ave')"

mycursor.execute(suppliers1)

suppliers2 = "INSERT INTO SupplyDB.Suppliers(sid, sname, address) VALUES(222, 'Linda Wang', '20 Main Street')"

mycursor.execute(suppliers2)

suppliers3 = "INSERT INTO SupplyDB.Suppliers(sid, sname, address) VALUES(333, 'Paul Justin', '150 Water Street')"

mycursor.execute(suppliers3)

suppliers4 = "INSERT INTO SupplyDB.Suppliers(sid, sname, address) VALUES(444, 'Andy Brown', '1 Elizabeth Ave')"

mycursor.execute(suppliers4)

suppliers5 = "INSERT INTO SupplyDB.Suppliers(sid, sname, address) VALUES(555, 'Bob Lee', '10 Governor Road')"

mycursor.execute(suppliers5)

suppliers6 = "INSERT INTO SupplyDB.Suppliers(sid, sname, address) VALUES(666, 'Lisa Reed', '10 Governor Road')"

mycursor.execute(suppliers6)

mydb.commit()
