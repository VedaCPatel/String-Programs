#Removal all characters from a string except integers
int=input("Enter a string: ")
r=""
for i in int:
    if i.isnumeric():
        r+=i
print("The integers mentioned in the string are: ",r)
