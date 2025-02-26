n=370
x=n
a=n%10
n=n//10
b=n%10
n=n//10
s=(n*n*n)+(b*b*b)+(a*a*a)
if x==s:
    print("Num is armstrong:")

else:
    print("Num is not armstrong:")
