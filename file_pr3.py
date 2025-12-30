with open("practice.txt","r") as f :
  data = f.read()
  data1 = data.split(',')
  print(data1)
  count = 0
  for i in range(len(data1)):
      data1[i] = int(data1[i])
      if(data1[i]%2 == 0):
        count += 1    

  print("The count of even numbers in file is: ",count)
