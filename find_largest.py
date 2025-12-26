def find_largest(list):

  large = list[1]
  for i in list :
    if large<i :
      large = i

  return large


list1 = [1,4,6534,324,-5,45]

print(f"The largest element from list {list1} is: ",max(list1))
print(f"The largest number in list {list1} is: ",find_largest(list1))