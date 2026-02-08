m1 = float(input("Enter marks: "))
m2 = float(input("Enter marks: "))
m3 = float(input("Enter marks: "))
m4 = float(input("Enter marks: "))
m5 = float(input("Enter marks: "))

marks = (m1+m2+m3+m4+m5)/5

if marks<=100 and marks>75 :
    print("Ditiction")
elif marks<=75 and marks>50 :
    print("First class")
elif marks<=50 and marks>=40 :
    print("Pass")
elif marks<40 and marks>=0 :
    print("Fail")
else :
    print("Invalid marks")
    
