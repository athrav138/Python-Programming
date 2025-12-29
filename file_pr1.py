#with open("practice.txt","w") as f:
# f.write("Hi everyone \nwe are learning file input ouput\nUsing Java\nI like Programming in Java.")

with open("practice.txt","r") as f:
  data = f.read()
  new_data=data.replace("Java","python")

with open("practice.txt","w") as f:
  f.write(new_data)