def is_substring(sub,str):
  return sub in str

str = input("Enter string:")
sub = input("Enter substring: ")

print("Substring is present: ",is_substring(sub,str))