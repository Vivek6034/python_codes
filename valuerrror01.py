# try:

#     age=int(input("Enter your age : "))
#     if(age<18):
#         raise ValueError
#     else:
#         print("you can voote ;")

# except ValueError:
#     print("not vote ;")

# try:
#     no=int(input("enteer posiitive no :"))
#     if(no<=0):
#         raise ValueError
#     else:
#         print("vote")
# except ValueError as e:
#     print(e)

try:

    a=12
    b=0
    if b is 0:
        raise ArithmeticError
    else:
        print(a/b)
except ArithmeticError:
    print("b is zero")