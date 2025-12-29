f = open("hello.txt","r")
"""
data = f.read() # TO read the all data in the file
print(type(data))
print(data)

data = f.read(10) # To read the first number of characters
print(data)

data = f.readline()  # To read the first line in the file
print(data)
"""

data = f.readlines()
print(data)
f.close()
