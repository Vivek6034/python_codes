import pymysql as mq
connnect = mq.connect(
    host='localhost',
    user='root',
    password="",
    database="student")
mycursor= connnect.cursor()
try:
    tdata="INSERT INTO stddata(name,roll,age,email) values(%s,%s,%s,%s)"
    td=("vivek","50","22","vivek@gmail.com")
    mycursor.execute(tdata,td)
    connnect.commit()
    print("Data inserted")

except:
    print("nhi huaa ")