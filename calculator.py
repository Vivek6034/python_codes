print("""
    + ADD
    - SUBTRACT
    * MULTIPLY
    / DIVIDE
""")
num1 = int(input("Enter a 1st num : = "))
num2 = int(input("Enter a 2nd num : = "))

opr = input("enter a operator ..( + , - , * , / ) ")

if opr == "+":
    print(num1 + num2)
elif opr== "-":
    print(num1-num2)
elif opr=="*":
    print(num1 * num2)
elif opr== "/":
    print (num1/num2)
else:
    print("Invalid Opr")