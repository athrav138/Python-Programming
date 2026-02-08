def gcd(n1,n2):
  if(n1>n2):
    if(n1%n2==0):
      return n2
    else:
      lis1 = set()
      for i in range(1,int(n1/2+1),1):
        lis1.add(i)
      lis2 = set()
      for i in range(1,int(n2/2+1),1):
        lis2.add(i)
      lis3  = lis1 & lis2
      return max(lis3)
  else :
    if(n2%n1==0):
      return n1
    else :
      lis1 = set()
      for i in range(1,int(n1/2+1),1):
        lis1.add(i)
      lis2 = set()
      for i in range(1,int(n2/2+1),1):
        lis2.add(i)
      lis3  = lis1 & lis2
      return max(lis3)

n1 = int(input("Enter number: "))
n2 = int(input("Enter number: "))

print(gcd(n1,n2))
