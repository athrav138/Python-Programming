
first_name = "Atharv "
middle_name = "Milind "
last_name = "Suryavanshi"

full_name = first_name + middle_name + last_name

print("Full name: ",full_name)
print("No. of Characters in name: ",len(full_name)-2)

# slicing a  string
slice = first_name[0:3]
slice1 = first_name[:3]
slice2 = first_name[0:]
print(slice)

# slicing using the negative indexing

slice3 = first_name[-(len(first_name)):-1]
print(slice3)

slice4 = last_name[-6:-1]

#   S   u    r  y  a  v  a  n  s  h  i
# -11  -10  -9 -8 -7 -6 -5 -4 -3 -2 -1

print(slice4)