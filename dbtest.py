import mysql.connector as mysql
import socket
hostname = socket.gethostname()
IP_address= socket.gethostbyname(hostname)

user =input("user: ")
db=mysql.connect(
    host=IP_address,
    user=user,
    port=3306,
    password="",
    database="pysql")
print("connected to: ", db.get_server_info())

