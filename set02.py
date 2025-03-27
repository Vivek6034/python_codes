s1={1,2,3,4,5,6}
s2 = {i for i in range (1,5)}
print(s2)
print(s1.intersection(s2))
print(s1.union(s2))
print(s1.difference(s2))
print(s2.difference(s1))
#wap to make  crud operation on set
while(True):
    ch = int(input("enter your choice : "))
    if ch==1:
        n= int(input("enter the no. of data = "))
        for i in range (n):
            data = input("enter the data ")
            s2.add(data)
    elif (ch==2):
            break
    
    elif ch==3:
        print(s2)

    elif(ch==4):
        n=int(input("enter the no .for  data remove = "))
        for i in range(n):
            data = input("enter the data : = ")
            s2.discard(data)

        
###distionary##################


