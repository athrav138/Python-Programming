list1 = [1,2,3,4,5,6]
list2 = [3,4,5,12,34,35]

# Common list elements in using Sets
def list_common(list1,list2):
    print(set(list1) & set(list2))

list_common(list1,list2)


# Common list elements using in operator
def list_common2(list1,list2):
    for i in list1 :
        if i in list2 :
            print(i)

list_common2(list1,list2)

