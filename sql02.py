import mysql.connector
mydb = dbtest.connector.connect(
    host='localhost',
    user='root',
    password=""
)
mycursor = mydb.cursor()
db="create database mydatabase"
mycursor.execute(db)
print("created")