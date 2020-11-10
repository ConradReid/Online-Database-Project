#!C:\Users\conra\AppData\Local\Programs\Python\Python38
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="ccharlesr",
    passwd="Haloreach98!",
    database="SupplyDB")

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE Parts(pid VARCHAR(20), pname VARCHAR(20), color VARCHAR(20))")
