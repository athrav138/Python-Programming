#This is the efficient method to find the gcd of two numbers
def gcd(n1,n2):    
    for i in range(min(n2,n1),0,-1):
      if n1%i==0 and n2%i==0:
        return i
     
n1 = int(input("Enter number: "))
n2 = int(input("Enter number: "))

print(gcd(n1,n2))

n =2
m = 3
print(m,n)
(n,m) = (m,n)
print(m,n)
