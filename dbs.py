import mysql.connector
print(" sql connected")
student = dbtest.connector.connect(
    host="localhost",
    user= "root",
    password="",
    database="student"


)
mycursor=student.cursor()
print("rms")