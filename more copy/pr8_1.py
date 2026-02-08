list = []

n = int(input("Enter number of items want in list: "))
for i in range(0,n,1):
  n = int(input())
  list.append(n)

print(list)

list.sort()
print(list)