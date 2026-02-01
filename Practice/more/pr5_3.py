print("Pattern 1:")

for i in range(6,0,-1):
    for j in range(1,i,1):
        if j%2==0:
            print("0",end=" ")
        else :
            print("1",end=" ")
    print()

print("Pattern 2: ")

for i in range(0,5,1):
    for j in range(0,i,1):
        print("*",end=" ")
    print()