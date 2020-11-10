#!C:\Users\conra\AppData\Local\Programs\Python\Python38\python.exe
import mysql.connector
import cgi

mydb = mysql.connector.connect(
    host="localhost",
    user="ccharlesr",
    passwd="Haloreach98!",
    database="SupplyDB")

mycursor=mydb.cursor()

form = cgi.FieldStorage()
print("Content-Type:text/html")
print()
if 'address' not in form:
    print('<h2>error</h2>')
    print('<p>please enter an address</p>')
else:
    print('<table align="center" border><tr><th>sid</th><th>sname</th></tr>')
    address = form['address'].value
    sql = 'select distinct S.sid, S.sname from Suppliers S '+\
          'where S.address ='+''+address+''+' and S.sid not in'+\
          '(select C.sid from Catalog C)'
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print('<tr><td>'+str(x[0])+'</td><td>'+str(x[1])+'</td></tr>')

    print('</table>')

