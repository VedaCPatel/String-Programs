#Find words with both alphabets and numbers
int=input("Enter a string: ")
l=int.split(" ")
print(l)
for i in l:
    d = 0
    c = 0
    for j in i:
        if j.isnumeric():
            d+=1
        if j.isalpha():
            c+=1
    if d>0 and c>0:
        print(i)


