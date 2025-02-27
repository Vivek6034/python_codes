a = int(input("enter the coff of x2 : "))
b = int(input("enter the coff of x :"))
c  = int(input("enter the constant :"))
d = (b*b-4*a*c)**0.5
r1 = (-b+d)/2*a
r2 = (-b-d)/2*a
print(f"roots are {r1} and {r2}")