with open("practice.txt","r") as f :
  data = [int(f.read())]
  count=0
  for i in data :
    if(i%2==0):
      count+=1

  print(count)
