#Arrange string characters such that lowercase letters should come first
s=input("Enter a string:")
a=""
for i in s:
    if i.islower():
        print(i,end="")
    else:
        a=a+i
print(a)

