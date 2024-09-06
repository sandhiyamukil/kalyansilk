#!C:\python\python.exe

import cgi
import mysql.connector

print("Content-Type:text/html\rn\rnr\n")

form=cgi.FieldStorage()
fname=form.getvalue("name")
fage=form.getvalue("age")
fcity=form.getvalue("city")  
fmobile=form.getvalue("mobile")  

print(fname,fage,fcity,fmobile)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="kalyansilk"
)

mycursor = mydb.cursor()

sql="INSERT INTO buyer(Name,age,city,mobile)VALUES(%s,%s,%s,%s)"
val=(fname,fage,fcity,fmobile)

mycursor.execute(sql,val)
mydb.commit()