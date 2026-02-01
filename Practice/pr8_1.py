list1 = [1,2,-34,56,234,67,3,4,5]

print(list1)
list1.sort()
print(list1)

def cmd(list1,list2):
    if list1>list2 :
        return 1
    elif list2>list1 :
        return -1 
    else :
        return 0

list1 = [1,2,3,774,5]
list2 = [1,2,3,46,5]

print(cmd(list1,list2))