#!C:\Users\conra\AppData\Local\Programs\Python\Python38\python.exe
import mysql.connector
import cgi
#import cgitb
#cgitb.enable()
mydb = mysql.connector.connect(
    host="localhost",
    user="ccharlesr",
    passwd="Haloreach98!",
    database="SupplyDB")

mycursor=mydb.cursor()
print("Content-Type:text/html")
print()
form = cgi.FieldStorage()
if 'pname' not in form:
    print('<h2>error</h2>')
    print('<p>please enter a part name</p>')
else:
    tableString = '<table align="center" border><tr>'
    sql = "select "
    if form.getvalue('sid'):
        tableString += '<th>sid</th>'
        sql += "S.sid"
    if form.getvalue('sname'):
        tableString += '<th>sname</th>'
        if form.getvalue('sid'):
            sql += ', S.sname'
        else:
            sql += 'S.sname'
            
    if form.getvalue('address'):
        tableString += '<th>address</th>'
        if form.getvalue('sid'):
            sql += ', S.address'
        elif form.getvalue('sname'):
            sql += ', S.address'
        else:
            sql += 'S.address'
            
    if form.getvalue('cost'):
        tableString += '<th>cost</th>'
        if form.getvalue('sid'):
            sql += ', C.cost'
        elif form.getvalue('sname'):
            sql += ', C.cost'
        elif form.getvalue('address'):
            sql += ', C.cost'
        else:
            sql += 'C.cost'

    pname = form['pname'].value
    #pname = str(pname)
    #this may have too many quotes
    #print(pname)
    sql += ' from Suppliers S, Parts P, Catalog C where C.pid = P.pid'+\
           " and C.sid = S.sid and P.pname ="+' '+pname+''
       
    print(tableString)

    
    
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        outputData = '<tr>'
        y = len(x)
        for i in range(y):
            outputData += '<td>'+str(x[i])+'</td>'

        outputData +='</tr>'
        #perhaps won't need the print()
        print(outputData)
        outputData =''
            
    print('</table>')        
        
        
    
