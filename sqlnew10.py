import sqlnew09
obj1= sqlnew09.dbconn()
while(True):
    ch = int(input("enter your choice :"))

    if(ch==1):
        name=input("enter the name : ")
        roll=input("enter your roll : ")
        age = input("enter your age : ")
        email=input("enter your email : ")
        obj1.Recordinsert(name , roll , age , email)  
    elif(ch==2):
        obj1.RecordDisplay()
    elif(ch==3):
        obj1.RecordUpdate()
    elif(ch==4):
        obj1.searchRecord() 
    elif(ch==5):
        obj1.DeleteRecord()
    elif(ch==6):
        print("closed")
    elif(ch==7):
        print("wrong choice")