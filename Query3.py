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
if 'pid' not in form:
    print('<h2>error</h2>')
    print('<p>please enter a pid</p>')
else:
    print('<table align="center" border><tr><th>sname</th><th>address</th></tr>')
    pid = form['pid'].value
    sql = 'select S.sname, S.address from Catalog C, Suppliers S where C.sid = S.sid '+\
          'and C.pid ='+''+pid+''+' and C.cost >= all(select C.cost from Catalog C'+\
          ' where C.pid ='+''+pid+''+')'
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print('<tr><td>'+str(x[0])+'</td><td>'+str(x[1])+'</td></tr>')
    
    print('</table>')
