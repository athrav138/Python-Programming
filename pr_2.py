
subject = {

}

x = int(input("Enter chem marks:"))
subject.update({"chem" : x})

x = int(input("Enter phy marks:"))
subject.update({"phy" : x})

x = int(input("Enter math marks:"))
subject.update({"math" : x})

print(subject)


set = {9,"9.0"} # the first solution is to store a one as stringS
print(set)

set1 = {("int",9),("flaot",9.0)}
print(set1)
