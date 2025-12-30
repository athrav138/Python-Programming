with open("practice.txt","r") as f :
  data = f.read()
  data1 = data.split(',')
  print(data1)
  for i in range(len(data1)):
      data1[i] = int(data1[i])
  print(data1)
  #print(count)
