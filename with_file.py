with open("hello.txt","r") as f:
  data = f.read()
  print(data)

with open("hello.txt","w") as f:
  f.write("NEw data")

with open("hello.txt","r") as f:
  data = f.read()
  print(data)