list = [1,2,3,4,5,6,7,8,9,10]
list2 = []
j = 0
print(list)

for i in list :
  list2.append(i) 

j = 0
for i in range(-1,-11,-1):
  list[j] = list2[i]
  j += 1

print(list)


list.reverse()
print(list)
