# To print the factorial of n number
def fact(n):
  if(n==0 or n==1):
    return 1
  else :
    return n*fact(n-1)
  
#n = int(input("ENter the number: "))
#print("Factorial of n is: ",fact(n))

# To print the numbers from n to 1
def print2(n):
    if n == 0:
        return 
    print(n)
    print2(n - 1)

#print(print2(n))

# To print the 1 to n numbers
def print1(n,s=1):
  
  if s==n :return n
  print(s)
  return print1(s+1,n)

#print(print1(n))

# To print the sum of 1 to n
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

#print("Sum is:", sum_n(n))


# To print the element in the list
def print_list_element(list,idx=0):
  if(idx==len(list)):
    return
  print(list[idx])
  return print_list_element(list,idx+1)

list = [1,2,3,4,5,6,7,8,9,10]

print_list_element(list)
   