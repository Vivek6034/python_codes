def noreturn_withargument(n=5):
    for i in range(n,0,-1):
        for j in range(1,i+1,1):
            print(i, end=" ")
        print()
hello=noreturn_withargument
hello()

def return_noargument():
    a=10
    b=20
    c=a+b
    d=a*b
    return c,d
x=return_noargument()
add=0
for i in x:
    add=add+i
print(add)