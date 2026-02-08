tuple1 = (1,2,3,45,5234,243,342)
tuple3 = ()   # Empty Tuple
tuple4 = (2)

print(tuple1[4])
print("Tuple is: ",tuple1)

del tuple3 # Deleting the tuple

list1 = list(tuple1)
print("tuple1 coverted to list: ",list1)

tuple2 = tuple(list1)
print("list1 coverted to tuple: ",tuple2)

print("Max in tuple: ",max(tuple1))
print(min(tuple1))