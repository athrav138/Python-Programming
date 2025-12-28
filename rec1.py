def fact(n):
  if(n==0 or n==1):
    return 1
  else :
    return n*fact(n-1)
  
n = int(input("ENter the number: "))
#print("Factorial of n is: ",fact(n))

def print2(n):
    if n == 0:
        return 
    print(n)
    print2(n - 1)


def print1(s,n):
  
  if s==n :return n
  print(s)
  return print1(s+1,n)

print(print2(n))
print(print1(1,n))