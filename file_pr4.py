with open("practice.txt","r") as f :
  count=1
  got = True

  while got :
    data = f.readline()
    if data.find('learning') != -1:
      print("The word learning is fount at line: ",count)
      got = False
      break
    count+=1

  
