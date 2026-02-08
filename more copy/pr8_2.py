list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [11,12,13,5,23,45,9,112]

common = set(list1) & set(list2)

for i in common :
  print(i)