import sqlnew09
obj1= sqlnew09.dbconn()
ch=int(input ("enter your choice :"))
if(ch==1):
    name=input("enter the name : ")
    roll=input("enter your roll : ")
    age = input("enter your age : ")
    email=input("enter your email : ")
    obj1.Recordinsert(name , roll , age , email)