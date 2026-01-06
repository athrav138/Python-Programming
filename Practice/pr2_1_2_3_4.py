import math
#  Write a program to find the square root of a number.

a = int(input("Enter a number to find square root: "))
print(math.sqrt(a))



# Write a program to convert bits to Megabytes, Gigabytes and Terabytes.

bits = int(input("ENter the number of bits: "))

MB = bits/(8*1000000)
print("In MB is: ",MB)

GB = bits/(8*1000000000)
print("In GB is: ",GB)

TB = bits/(8*1000000000000)
print("In TB is: ",TB)



# Write a program to swap the value of two variables

a = 2 
b = 3
print(f"Before swap a={a} and b={b}")
c = a
a = b
b = c
print(f"After swap a={a} and b={b}")


# Write a program to calculate surface volume and area of a cylinder


height = float(input("Enter height of cylinder: "))
radius = float(input("Enter radius of cylinder: "))


volume = math.pi * radius * radius * height
s_area = 2 * math.pi * radius * (radius + height)


print("THe area of cylinder is: ",s_area,", sq. units")
print("THe surface volume of cylinder is: ",volume,", cu. units")