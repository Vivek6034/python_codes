class dbconn:
    def __init__(self):
        import mysql.connector
        mydb= mysql.connector.connect(
            host="localhost",
            user="root",
            password = "",
            database="student"
        )
        self.mycursor=self.mydb.cursor()
        def Recordinsert(self,name , roll , age , email):
            self.name=name
            self.roll=roll
            self.age=age
            self.email=email
            sql="INSERT INTO stu_data(name,roll,age,email) VALUES(%s,%s,%s,%s)"
            value=[self.name, self.roll,self.age,self.email]
            self.mycursor.execute(sql,value)
            self.mydb.commit()
            