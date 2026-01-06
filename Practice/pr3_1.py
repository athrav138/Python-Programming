# Write a program to check the largest number among the three numbers 

n1 = int(input("ENter first number: "))
n2 = int(input("ENter second number: "))
n3 = int(input("ENter third number: "))

if(n1>n2 and n1>n3):
    print(f"n1 = {n1} is largest")
elif(n2>n1 and n2>n3):
    print(f"n2 = {n2} is largest")
else:
    print(f"n3 = {n3} is largest")