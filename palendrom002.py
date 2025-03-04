n1= int(input("enter the no : "))
n2 = int(input("no of palendrom you want"))
i=1
n1+=1
while(i<=n2):
    temp=n1
    rev = 0
    while(temp>0):
        r=temp%10
        rev = rev*10+r
        temp = temp //10
        if(rev==n1):
            print("palendrom",rev)
            i+=1
    n1+=1
    

#wap using choise based user can exit from the program only if user can press 5