#wap to add first 10 natural number using while loop
n=int(input("Enter a number"))
i=1
sum_even = 0
sum_odd = 0
while(i<=n):
    if(i%2==0):
     sum_even=sum_even+i
    
    else:
       sum_odd=sum_odd+i
    i+=1

print("sum_even",sum_even)