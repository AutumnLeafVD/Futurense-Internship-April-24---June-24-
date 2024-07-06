import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="123",
    database="myuni"
    )

print(mydb)

mycursor=mydb.cursor()
mycursor.execute("show tables")

for x in mycursor:
    print(x)
    
