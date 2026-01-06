def count_vowels(str):
  str = str.lower()
  count = 0
  
  for i in range(len(str)):
    if str[i]=='a' or str[i]=='e' or str[i]=='i' or str[i]=='o' or str[i]=='u' :
      count += 1

  return count

string = "Alaioue"

print("The number of vowels in {string} is: ",count_vowels(string))