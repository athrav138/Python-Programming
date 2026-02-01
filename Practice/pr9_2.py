tuple1 = (1,2,23,4,56,443,53,632452,35,234,5)

# Using list() function
print(list(tuple1))

# Using for loop
list1 = []
for i in tuple1 :
    list1.append(i)
print(list1)

# List comprehension
list2 = [i for i in tuple1]
print(list2)

# Using * operator
list3 = [*tuple1]
print(list3)

# Usinhg the map() function 
list4 = list(map(lambda x:x,tuple1))
print(list4)

