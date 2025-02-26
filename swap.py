# wap to swap the two variable without
#  using third variable and without using airthmatic operration

x=20
y=40

print(f"Before swapping the value of x ={x} and y ={y}")
x,y=y,x
print(f"After swapping the value of x ={x} and y ={y}")

# swap of two variable using third variable

a = 10
b = 20

print(f"Before swapping the value of a ={a} and b ={b}")

temp = a
a= b 
b = temp
print(f"After swapping the value of a ={a} and b ={b}")


# swap of two variable using airthmatic operration

a = int(input("Enter the first number :"))
b = int (input("Enter the second Number : "))

print(f"before swaping : a= {a} and b={b}")

a = a+b
b = a-b
a = a-b
print(f"After swapping : a={a} and b= {b}")