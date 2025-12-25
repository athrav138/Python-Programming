
name = ["Atharv","Rucha","Milind","Sujata","Chabutai","Tukaram"]

"""
for i in name :
  print(i)

for i in range(len(name)):
  print(name[i])
"""

name[1] = "Aps"

print(name)
print(name[1])
print("The type is: ",type(name))

print(name[1:3])
print(name)
name1 = name[1:3]
print(name1)
print(name[-3:-1])

# Built in functions on the lists 

# append function
name1.append("Helo")
print(name1)

# Sort function
name1.sort()
print(name1)

# sort reverse using the sort function
name1.sort(reverse=True)
print(name1)

# reversing the list using the reverse funciton
name1.reverse();
print(name1)

# Inserting the data in the list
name1.insert(5,12)
name1.insert(4,"hello")
name1.insert(3,45)
print(name1)



