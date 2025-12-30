with open("practice.txt","r") as f :
  count=1
  got = True

  while got :
    data = f.readline()
    if 'learning' in data:
      print("The word learning is fount at line: ",count)
      got = False
      break
    count+=1

  
