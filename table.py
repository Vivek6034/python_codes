# n=int(input("enter any nnumber"))

# i=1
# while(i<=10):
#     print(n, "*",i ,"=",n*i)
#     i+=1
ls = [12, 2, 6, 8, 7, 9, 5, 84, 1, 425]

for i in range(len(ls)):
    for j in range(0, len(ls) - i - 1):
        if ls[j] > ls[j + 1]:
            ls[j], ls[j + 1] = ls[j + 1], ls[j]

print(ls)
 