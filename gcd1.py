def gcd(n1,n2):
  if(n1>n2):
    if(n2%n1==0):
      return n1
    for i in range(n2,1,-1):
      if n1%i==0 and n2%i==0:
        return i
  else :
    if(n2%n1==0):
      return n1
    for i in range(n1,1,-1):
      if n1%i==0 and n2%i==0:
        return i
     

n1 = int(input("Enter number: "))
n2 = int(input("Enter number: "))

print(gcd(n1,n2))
