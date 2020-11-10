#!C:\Users\conra\AppData\Local\Programs\Python\Python38\python.exe
import mysql.connector
import cgi

mydb = mysql.connector.connect(
    host="localhost",
    user="ccharlesr",
    passwd="Haloreach98!",
    database="SupplyDB")

mycursor=mydb.cursor()
print("Content-Type:text/html")
print()
form = cgi.FieldStorage()
if 'color' not in form:
    print('<h2>error</h2>')
    print('<p>please enter a color</p>')
elif 'address' not in form:
    print('<h2>error</h2>')
    print('<p>please enter an address</p>')
else:
    print('<table align="center" border><tr><th>pname</th></tr>')
    color = form['color'].value
    address = form['address'].value
    sql = 'select distinct P.pname from Catalog C, Suppliers S, Parts P '+\
          'where C.sid = S.sid and P.pid = C.pid '+\
          'and P.color ='+''+color+''+' and S.address ='+''+address+''
    mycursor.execute(sql)
    myresult= mycursor.fetchall()
    for x in myresult:
        print('<tr><td>'+str(x[0])+'</td></tr>')

    print('</table>')
    
    
