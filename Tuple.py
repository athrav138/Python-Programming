
tuple = (4,12, 453, 454, 54, 46, 7, 8, 9, 10, 11, 12, 13, 14, 15)

for i in tuple:
  print(i)

for i in range(len(tuple)):
  print(tuple[i])

print(tuple)

print("The type is: ",type(tuple))

print("Index of 54 is: ",tuple.index(54))

print("Count of 12 is: ",tuple.count(12))