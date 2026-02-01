n = input("Enter a number: ")

words = {
    '0' : 'Zero',
    '1' : "One",
    '2' : "Two",
    '3' : "Three",
    '4' : "Four"
}

for i in n:
    print(words[i],end=" ")

dict = {
    "Shreyash" : "Sutar"
}

print(dict["Shreyash"])