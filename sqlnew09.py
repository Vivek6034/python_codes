import pymysql as mq

class dbconn:
    def __init__(self):
        self.mydb = mq.connect(
            host="localhost",
            user="root",
            password="",
            database="student")
        self.mycursor = self.mydb.cursor()

    def Recordinsert(self, name, roll, age, email):
        try:
            sql = "INSERT INTO stddata(name, roll, age, email) values (%s, %s, %s, %s)"

            td = [name, roll, age, email]
            self.mycursor.execute(sql, td)
            self.mydb.commit()
            print(" Record inserted")
        except :
            print(" MySQL error:")
    def RecordDisplay(self):
        sql="select * from stddata"
        self.mycursor.execute(sql)
        mydata=self.mycursor.fetchall()
        for i in mydata:
            print(i)
    def RecordUpdate(self):
        old_name=input("enter old name :")
        name=input("enter name :")
        roll=input("enter roll no : ")
        age = input("enter your age : ")
        email= input("enter your email : ")

        sql="update stddata set name=%s,roll=%s,age=%s,email=%s where name=%s"
        value=[name,roll,age,email,old_name]
        self.mycursor.execute(sql,value)
        self.mydb.commit()
        print("record updated ")
    def searchRecord(self):
        roll=input("enter the roll no : ")
        sql= "select * from stddata where roll=%s"
        value=[roll]
        self.mycursor.execute(sql,value)
        mydata=self.mycursor.fetchall()
        count=self.mycursor.rowcount
        if count>=1:
            print(mydata)
        else:
            print("Record not Found")

    def DeleteRecord(self):
        roll=input("enter your roll no :")
        sql=" delete from stddata where roll=%s"
        value=[roll]
        self.mycursor.execute(sql,value)
        self.mydb.commit()
        print("data khtm")
        
    
