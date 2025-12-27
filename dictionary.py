student_marks = {} # empty dictionary

student_marks = {
  "Atharv" : 98,
  "Rucha" : 82,
  "Sujata" : 63,
  "Milind" : 55
}

print(student_marks)

# methods on the dictionary

# prints the all items in the dictionary
print(student_marks.items())

# Used to get the value of particular item
print(student_marks.get("Rucha"))

# Delets the particular value in the dictionary
student_marks.pop("Milind")
print(student_marks)

# Used to update the value of item
student_marks.update({"Rucha":80})
print(student_marks)

# to print the all items in the dictionary 
student_marks.values()

# to print the size of dictionary in the bytes\
print("The size of the dictionary is: ",student_marks.__sizeof__())


# deletes the all the data int the dictionary 
student_marks.clear()
print(student_marks)


