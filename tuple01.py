tup1=(1,2,3,4,5,6,8,9)
print(tup1)
print(type(tup1)) #print type of tuple
x=max(tup1)
print(x)
ls= list(tup1) #covert tuple to list
print(ls)
tup1 = tuple(ls)  #convert list to tuple
print(tup1)
#wap to make a crud operation on tuple

while(True):
    ch = int(input("enter your choice : "))
    if ch==1:
        n= int(input("enter the no. of data = "))
        for i in range (n):
            data = input("enter the data ")
            ls.append(data)
            tup1 = tuple(ls)  #convert list to tuple

    elif(ch==2):
        print(ls)
        print(tup1)
    elif(ch==3):
        n=int(input("enter the no .for  data remove = "))
        for i in range(n):
            data = input("enter the data : = ")
            ls.remove()
            tup1 = tuple(ls)  #convert list to tuple
    elif(ch==4):
        break

