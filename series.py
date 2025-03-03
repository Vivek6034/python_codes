n = int(input("Enter the number of terms: "))

ans = 0
i = 1  
while i <= n:
    if i % 2 == 1:  
        ans += i
    else:  
        ans -= i
    i += 1  

print(f"The result of the series is: {ans}")