#wap to find area of all the shapes 
#input taken from user

#--------AREA OF THE SQUARE----#
side = float(input("Enter the side square : "))
area = side*side
print("Area of sqaure is ", area)


print("=====================================")
print("=====================================")
 

# -------------AREA OF THE RECTANGLE-------#
l = float(input("Enter the length of Rectangle :"))
w= float(input("Enter the width of Rectangle :"))
Area_of_Rectangle = l*w
print("Area of Reactangle = ",Area_of_Rectangle)


print("=====================================")
print("=====================================")



#------AREA OF TRIANGLE------#
b= float(input("Enter the base of triangle :"))
h=float(input("Enter the height of triangle :"))
area_of_triangle = 1/2*b*h
print("Area of Triangle = ", area_of_triangle)

print("=====================================")
print("=====================================")


#------AREA OF CIRCLE----#

r = float(input("Enter the redius of circle : "))
area_of_circle = 3.14*r*r
print("Area of circle = ",area_of_circle)

print("=====================================")

print("=====================================")


#----AREA OF RHOMBUS---#

d1 = float(input("Enter first Diagonal length : "))
d2 = float(input("Enter second Diagonal length : "))

area_of_rhombus=(d1*d2)/2
print("Area of rhombus = ",area_of_rhombus)

