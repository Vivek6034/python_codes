import mysql.connector
print("connection seccefull")

mydb= mysql.connector.connect(
    host="localhost",
    user="vivek",
    password="Vivek123@",
    database="crudpython"
)
mycursor = mydb.cursor()
print("rms")