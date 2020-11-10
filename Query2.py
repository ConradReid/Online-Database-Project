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

if 'cost' not in form:
    print('<h2>error</h2>')
    print('<p>please enter a cost</p>')
else:
    print('<table align="center" border><tr><th>sname</th></tr>')
    cost = form['cost'].value
    #cost = int(cost)
    sql = 'select distinct S.sname from Suppliers S, Catalog C where C.sid = S.sid '+\
          'and C.cost >= '+''+cost+''
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print('<tr><td>'+str(x[0])+'</td></tr>')
        
    print('</table>')
