p = float(input("Enter the Physics marks: "))
c = float(input("Enter the Chemistry marks: "))
m = float(input("Enter the Mathematics marks: "))
h = float(input("Enter the Hindi marks: "))
e = float(input("Enter the English marks: "))

total_marks = p + c + m + h + e
per = total_marks / 5

if p < 0 or c < 0 or m < 0 or h < 0 or e < 0 or p > 100 or c > 100 or m > 100 or h > 100 or e > 100:
    print("Invalid marks")
    print("Physics=", p, "Chemistry=", c, "Mathematics=", m, "Hindi=", h, "English=", e)

elif (p < 33 and c >= 33 and m >= 33 and h >= 33 and e >= 33) or \
     (p >= 33 and c < 33 and m >= 33 and h >= 33 and e >= 33) or \
     (p >= 33 and c >= 33 and m < 33 and h >= 33 and e >= 33) or \
     (p >= 33 and c >= 33 and m >= 33 and h < 33 and e >= 33) or \
     (p >= 33 and c >= 33 and m >= 33 and h >= 33 and e < 33):
    
    if p < 33:
        print("Fail in Physics")
    if c < 33:
        print("Fail in Chemistry")
    if m < 33:
        print("Fail in Mathematics")
    if h < 33:
        print("Fail in Hindi")
    if e < 33:
        print("Fail in English")
    
    print("Physics=", p, "Chemistry=", c, "Mathematics=", m, "Hindi=", h, "English=", e)
    print("Total Marks =", total_marks)
    print("Percentage =", per, "%")
    print("Result: Fail")

elif (p < 33 and c < 33 and m >= 33 and h >= 33 and e >= 33) or \
     (p < 33 and c >= 33 and m < 33 and h >= 33 and e >= 33) or \
     (p < 33 and c >= 33 and m >= 33 and h < 33 and e >= 33) or \
     (p < 33 and c >= 33 and m >= 33 and h >= 33 and e < 33) or \
     (p >= 33 and c < 33 and m < 33 and h >= 33 and e >= 33) or \
     (p >= 33 and c < 33 and m >= 33 and h < 33 and e >= 33) or \
     (p >= 33 and c < 33 and m >= 33 and h >= 33 and e < 33) or \
     (p >= 33 and c >= 33 and m < 33 and h < 33 and e >= 33) or \
     (p >= 33 and c >= 33 and m < 33 and h >= 33 and e < 33) or \
     (p >= 33 and c >= 33 and m >= 33 and h < 33 and e < 33):
    
    if p < 33 and c < 33:
        print("Fail in Physics and Chemistry")
    elif p < 33 and m < 33:
        print("Fail in Physics and Mathematics")
    elif p < 33 and h < 33:
        print("Fail in Physics and Hindi")
    elif p < 33 and e < 33:
        print("Fail in Physics and English")
    elif c < 33 and m < 33:
        print("Fail in Chemistry and Mathematics")
    elif c < 33 and h < 33:
        print("Fail in Chemistry and Hindi")
    elif c < 33 and e < 33:
        print("Fail in Chemistry and English")
    elif m < 33 and h < 33:
        print("Fail in Mathematics and Hindi")
    elif m < 33 and e < 33:
        print("Fail in Mathematics and English")
    elif h < 33 and e < 33:
        print("Fail in Hindi and English")
    
    print("Physics=", p, "Chemistry=", c, "Mathematics=", m, "Hindi=", h, "English=", e)
    print("Total Marks =", total_marks)
    print("Percentage =", per, "%")
    print("Result: Fail")

elif (p < 33 and c < 33 and m < 33 and h >= 33 and e >= 33) or \
     (p < 33 and c < 33 and m >= 33 and h < 33 and e >= 33) or \
     (p < 33 and c < 33 and m >= 33 and h >= 33 and e < 33) or \
     (p < 33 and c >= 33 and m < 33 and h < 33 and e >= 33) or \
     (p < 33 and c >= 33 and m < 33 and h >= 33 and e < 33) or \
     (p < 33 and c >= 33 and m >= 33 and h < 33 and e < 33) or \
     (p >= 33 and c < 33 and m < 33 and h < 33 and e >= 33) or \
     (p >= 33 and c < 33 and m < 33 and h >= 33 and e < 33) or \
     (p >= 33 and c < 33 and m >= 33 and h < 33 and e < 33) or \
     (p >= 33 and c >= 33 and m < 33 and h < 33 and e < 33):
    
    if p < 33 and c < 33 and m < 33:
        print("Fail in Physics, Chemistry, and Mathematics")
    elif p < 33 and c < 33 and h < 33:
        print("Fail in Physics, Chemistry, and Hindi")
    elif p < 33 and c < 33 and e < 33:
        print("Fail in Physics, Chemistry, and English")
    elif p < 33 and m < 33 and h < 33:
        print("Fail in Physics, Mathematics, and Hindi")
    elif p < 33 and m < 33 and e < 33:
        print("Fail in Physics, Mathematics, and English")
    elif p < 33 and h < 33 and e < 33:
        print("Fail in Physics, Hindi, and English")
    elif c < 33 and m < 33 and h < 33:
        print("Fail in Chemistry, Mathematics, and Hindi")
    elif c < 33 and m < 33 and e < 33:
        print("Fail in Chemistry, Mathematics, and English")
    elif c < 33 and h < 33 and e < 33:
        print("Fail in Chemistry, Hindi, and English")
    elif m < 33 and h < 33 and e < 33:
        print("Fail in Mathematics, Hindi, and English")
    
    print("Physics=", p, "Chemistry=", c, "Mathematics=", m, "Hindi=", h, "English=", e)
    print("Total Marks =", total_marks)
    print("Percentage =", per, "%")
    print("Result: Fail")

elif (p < 33 and c < 33 and m < 33 and h < 33 and e >= 33) or \
     (p < 33 and c < 33 and m < 33 and h >= 33 and e < 33) or \
     (p < 33 and c < 33 and m >= 33 and h < 33 and e < 33) or \
     (p < 33 and c >= 33 and m < 33 and h < 33 and e < 33) or \
     (p >= 33 and c < 33 and m < 33 and h < 33 and e < 33):
    
    if p < 33 and c < 33 and m < 33 and h < 33:
        print("Fail in Physics, Chemistry, Mathematics, and Hindi")
    elif p < 33 and c < 33 and m < 33 and e < 33:
        print("Fail in Physics, Chemistry, Mathematics, and English")
    elif p < 33 and c < 33 and h < 33 and e < 33:
        print("Fail in Physics, Chemistry, Hindi, and English")
    elif p < 33 and m < 33 and h < 33 and e < 33:
        print("Fail in Physics, Mathematics, Hindi, and English")
    elif c < 33 and m < 33 and h < 33 and e < 33:
        print("Fail in Chemistry, Mathematics, Hindi, and English")
    
    print("Physics=", p, "Chemistry=", c, "Mathematics=", m, "Hindi=", h, "English=", e)
    print("Total Marks =", total_marks)
    print("Percentage =", per, "%")
    print("Result: Fail")

elif p < 33 and c < 33 and m < 33 and h < 33 and e < 33:
    print("Fail in all subjects")
    print("Physics=", p, "Chemistry=", c, "Mathematics=", m, "Hindi=", h, "English=", e)
    print("Total Marks =", total_marks)
    print("Percentage =", per, "%")
    print("Result: Fail")

else:
    if per < 45:
        print("3rd Division")
    elif per < 60:
        print("2nd Division")
    else:
        print("1st Division")
    
    print("Physics=", p, "Chemistry=", c, "Mathematics=", m, "Hindi=", h, "English=", e)
    print("Total Marks =", total_marks)
    print("Percentage =", per, "%")
    print("Result: Pass")