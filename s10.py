#Replace each special symbol with # in the following string
int=input("Enter a string: ")
j=""
for i in int:
    if i.isnumeric() or i.isalpha() or i==" ":
        j+=i
    else:
        j+="#"
print(j)