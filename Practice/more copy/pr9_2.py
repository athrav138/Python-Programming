tuple1 = (1,2,3,9,1,1,7,3,9)

print("Tuple is: ",tuple1)

repeated = set()

for i in tuple1 :
  if tuple1.count(i)>1 :
    repeated.add(i)

for i in repeated :
  print(i)