#!C:\Users\conra\AppData\Local\Programs\Python\Python38
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "ccharlesr",
    passwd = "Haloreach98!")

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE SupplyDB")


