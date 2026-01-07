list = [1]

for i in range (1,11):
  print(i*i)
  list.append(i*i)

for i in range(len(list)):
  print(list[i])


tuple = (1,2,3,4,564,23,5,-23,4522,5)


# Using lenear search
key = 5
i = 0
while key!=tuple[i]:
  i+=1
else :
 print(f"{key} is the key found in tuple at {i+1} postion")
