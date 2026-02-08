list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [11,12,13,5,23,45,9,112]

print("Following are the common values in the both lists:")
for i in list1:
  if(i in list2):
    print(f"{i}")