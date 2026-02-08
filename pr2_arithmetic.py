n1 = int(input("Enter number 1 :"))
n2 = int(input("Enter number 2:"))

             
sum = n1 + n2
print(f"addition of n1={n1} and n2={n2} is: ",sum)

sub = n1 - n2
print(f"Subtraction of n1={n1} and n2={n2} is: ",sub)

if n2==0 :
    print("Division is not possible")
else :
    div = n1/n2
    print(f"Division of n1={n1} and n2={n2} is: ",div)

mul = n1 * n2
print(f"Multiplication of n1={n1} and n2={n2} is: ",mul)
    
