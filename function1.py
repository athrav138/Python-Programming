# To find the average of three numbers
def avg(a,b,c):
  return (a+b+c)/3

print("The average is: ",avg(3,4,5))

# To find the length of list
def find_len(list):
  return len(list)

list1 = [1,2,3,5,5]
print("The length of list is:",find_len(list1))

# covert the amount from USD to INR
def covert_amount(usd):
  return usd*89.81

print("The amount from USD To INR",covert_amount(1))

# To print the numbers is even or odd
def ev_od(a):
  if a%2==0 :
    print("EVEN")
  else :
    print("ODD")

ev_od(2)