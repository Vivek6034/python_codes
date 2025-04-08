import pymysql as mq
myobj = mq.connect(host='localhost',user='root',password="")
cursor_obj = myobj.cursor()
try:
    db="create database school"
    cursor_obj.execute(db)
    print("Database created")


except:
    print("database erro..")