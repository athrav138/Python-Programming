def unique_string(str):
  return len(set(str))== len(str)

def unique_string1(str):
  return str.equals(set(str))

str = input("Enter string: ")
print(f"The all string characters are unique: ",unique_string(str))
print(f"The all string characters are unique: ",unique_string1(str))