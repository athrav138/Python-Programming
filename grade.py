marks = int(input("Enter a marks: "))

if marks<=100 and marks>=75 :
    print("Distinction")
elif marks<75 and marks>=65 :
    print("First class")
elif marks<65 and marks>=55:
    print("Second class")
elif marks<55 and marks>=40:
    print("pass")
elif marks<40 and marks>=0 :
    
    print("fail")
else :
    print("Invalid marks")
