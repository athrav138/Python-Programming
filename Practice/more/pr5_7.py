n = int(input("Enter a number: "))

f0 = 0
f1 = 1

print(f0)
print(f1)

for i in range(1,n-1):
    fnext = f0 + f1
    print(fnext)
    f0 = f1
    f1 = fnext