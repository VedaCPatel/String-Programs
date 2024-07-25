# Count all letters, digits, and special symbols from a given string
s = input("Enter a string:")
l=0
d=0
ss=0
for i in s:
    if i.isalpha():
        l+=1
    elif i.isnumeric():
        d+=1
    else:
        ss+=1
print("Letters:",l)
print("Digits:",d)
print("Special symbols:",ss)

