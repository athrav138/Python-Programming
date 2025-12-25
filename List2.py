
list = ["Atharv","Rucha","Atharv"]

reverse = []
reverse = list.copy()
reverse.reverse()
count = 0
print(list)
print(reverse)


"""
for i in range(len(list)):
  if list[i]!=reverse[i] :
    print("The list is not palindrome")
    count = 1
    break

if count == 0 : print("palit")

"""

if list == reverse :
  print("palindrome")
else :
  print("not Palindrome")
