#!C:\Users\conra\AppData\Local\Programs\Python\Python38
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="ccharlesr",
    passwd="Haloreach98!",
    database="SupplyDB")

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE Suppliers(sid INT, sname VARCHAR(20), address VARCHAR(20))")


