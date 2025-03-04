#when we declare moore than one lop inside the  another loop the
#  that type of condition is known as nested loop
#syntax:
#initalization of outer loop 
#while(condition):
        #initialization of inner loop
        #while (condition):
                #inc/dec of inner looop
        #inc/Dec of outer loop
i=1
while(i<=4):
    print("loop chla" ,i)
    j=1
    while(j<=5):
        print("inner roop chala" , j , end=" ")
        j+=1
    i+=1