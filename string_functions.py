string = "my name is atharv rucha"

# Check if string ends with given word (case-sensitive)
print("Ends with 'rucha':", string.endswith("rucha"))

# Capitalize first character of the string
print("Capitalized string:", string.capitalize())

# Replace character 'a' with 'o'
string = string.replace('a', 'o')
print("After replace:", string)

# Used to find the specific string in the another string

print(string.find('rucho'))

# print the count of substring occurance
print(string.count('o'))
