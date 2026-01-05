marks = float(input("Enter marks: "))

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
    
