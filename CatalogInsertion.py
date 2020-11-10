#!C:\Users\conra\AppData\Local\Programs\Python\Python38
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="ccharlesr",
    passwd="Haloreach98!",
    database="SupplyDB")

mycursor=mydb.cursor()

catalog1 = "INSERT INTO SupplyDB.Catalog(sid, pid, cost)"+ \
           "VALUES(111, 'P1', 300)"

mycursor.execute(catalog1)

catalog2 = "INSERT INTO SupplyDB.Catalog(sid, pid, cost)"+ \
           "VALUES(111, 'P3', 50)"

mycursor.execute(catalog2)

catalog3 = "INSERT INTO SupplyDB.Catalog(sid, pid, cost)"+ \
           "VALUES(111, 'P4', 500)"

mycursor.execute(catalog3)

catalog4 = "INSERT INTO SupplyDB.Catalog(sid, pid, cost)"+ \
           "VALUES(222, 'P1', 350)"

mycursor.execute(catalog4)

catalog5 = "INSERT INTO SupplyDB.Catalog(sid, pid, cost)"+ \
           "VALUES(222, 'P2', 200)"

mycursor.execute(catalog5)

catalog6 = "INSERT INTO SupplyDB.Catalog(sid, pid, cost)"+ \
           "VALUES(222, 'P3', 70)"

mycursor.execute(catalog6)

catalog7 = "INSERT INTO SupplyDB.Catalog(sid, pid, cost)"+ \
           "VALUES(222, 'P5', 30)"

mycursor.execute(catalog7)

catalog8 = "INSERT INTO SupplyDB.Catalog(sid, pid, cost)"+ \
           "VALUES(333, 'P2', 210)"

mycursor.execute(catalog8)

catalog9 = "INSERT INTO SupplyDB.Catalog(sid, pid, cost)"+ \
           "VALUES(333, 'P3', 56)"

mycursor.execute(catalog9)


catalog10 = "INSERT INTO SupplyDB.Catalog(sid, pid, cost)"+ \
           "VALUES(444, 'P1', 350)"

mycursor.execute(catalog10)

catalog11 = "INSERT INTO SupplyDB.Catalog(sid, pid, cost)"+ \
           "VALUES(444, 'P2', 300)"

mycursor.execute(catalog11)

catalog12 = "INSERT INTO SupplyDB.Catalog(sid, pid, cost)"+ \
           "VALUES(444, 'P3', 48)"

mycursor.execute(catalog12)

catalog13 = "INSERT INTO SupplyDB.Catalog(sid, pid, cost)"+ \
           "VALUES(444, 'P4', 550)"

mycursor.execute(catalog13)

catalog14 = "INSERT INTO SupplyDB.Catalog(sid, pid, cost)"+ \
           "VALUES(444, 'P5', 29)"

mycursor.execute(catalog14)

catalog15 = "INSERT INTO SupplyDB.Catalog(sid, pid, cost)"+ \
           "VALUES(555, 'P3', 65)"

mycursor.execute(catalog15)

catalog16 = "INSERT INTO SupplyDB.Catalog(sid, pid, cost)"+ \
           "VALUES(555, 'P4', 600)"

mycursor.execute(catalog16)
mydb.commit()
