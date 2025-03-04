n=int(input("enter a number :"))

cnt = 0
i=1

while(i<=n):
    if(n%i==0):
        cnt+=1
    i+=1
if(cnt==2):
    print("no is prime")
else:
    print("not prime")
     