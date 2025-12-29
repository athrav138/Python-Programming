
f = open("hello.txt","w")
f.write("HELLO WORLD")
f.close()

f = open("hello.txt","r")
data = f.read()
print(type(data))
print(data)
f.close()
