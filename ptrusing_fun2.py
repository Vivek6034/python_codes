def return_withargument(a,b):
    c=a+b
    d=a*b
    return c, d
x=return_withargument(10,20)
add = 0
for i in x:
    add=add+i
print(add)