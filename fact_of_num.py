#wap to find factorial of anu number;

n=int(input("enter the number"))
i=1
sum=1
while i<=n:
    sum*= i
    i+=1
print("fact of number is ",sum)
    
#find the sum of fact 1 + fact 2 + fact 3 input taken form user
n=int(input("enter the number"))
i=1
sum=0
while i<=n:
    sum= sum +i
    i= i+ 1
print("Sum of number is ",sum)
    
#sum of fact

m=int(input("enter aa number"))
j=1
fact=1
sum_fact=0
while(i<=n):
    fact = fact*i
    sum_fact = sum_fact+fact
    i+=1
#user  2 value  insert karega hame o/p first value k bad 2nd value tak k palendrom num show karna haig