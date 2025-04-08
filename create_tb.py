import pymysql as mq
connect = mq.connect(
    host='localhost',
    user='root',
    password="",
    database="school")

mysqlcur = connect.cursor()

ct="create table newstudent (st_id INT primary key auto_increment, st_name varchar(50), st_class varchar(10),st_email varchar(50))"
try:
    ins="INSERT INTO newstudent(st_name,st_class,st_email) values(%s,%s,%s)"
    t=[("vivek","12th","vivek@gmail.com"),("asshu","42th","aashu@gmail.com")]
    mysqlcur.executemany(ins,t)
    connect.commit()
    print("Data inserted")
except:
    print("Bhai kuchh galat hai")