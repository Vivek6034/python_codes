a = int(input("enter the no1: "))
b= int(input("enter the 2nd no : "))
try:
    c=a/b
except:
    print("cannot divide by 0 ! ")
else:
    print(c)
finally:
    print("division successsful")