tuple1 = [1,2,45,2,1,34,1]
list1 = []

# Using the list
for i in tuple1 :
    if (tuple1.count(i)>1 and i not in list1):
        list1.append(i)
print(list1)

# Using the set
set1 = set()
print()
for i in tuple1 :
    if (tuple1.count(i)>1 ):
        set1.add(i)
print(set1)