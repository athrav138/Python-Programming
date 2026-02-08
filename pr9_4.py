tuple1 = (1,2,3,4,5,6,7,8,9,0)
tuple2 = ('One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Zero')

s = input("Enter a number: ")
out = []
for ch in s:
    if ch.isdigit():
        if ch == '0':
            out.append(tuple2[9].lower())
        else:
            out.append(tuple2[int(ch)-1].lower())
print(' '.join(out))
