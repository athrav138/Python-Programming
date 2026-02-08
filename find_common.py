def find_common(list1,list2):
  return list(set(list1) & set(list2))

list1 = [1,2,3,4,5]
list2 = [12,34,5,3]
print(find_common(list1,list2))