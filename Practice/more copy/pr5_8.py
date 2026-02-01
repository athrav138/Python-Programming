num = int(input("Enter a number: "))
temp = num
rev = 0

while num!= 0 :
    rem = num % 10
    rev += rem
    num //= 10

print("The sum of digits of number is: ",rev)