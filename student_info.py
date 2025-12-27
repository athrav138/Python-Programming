# nesting of the dictionaries 

student_info = {
  "name" : ["ATHARV","RUCHA"],
  "subjects" : {
    "phy" : [96,97],
    "chem" : [89,59],
    "math" : [94.45]
  }
}

print(student_info)

print(student_info["subjects"]["math"]) # Accessing the single value in nesting dictionaries