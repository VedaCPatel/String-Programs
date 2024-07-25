#Create a string made of the first, middle and last character
s=input("Enter a string:")
l=len(s)
if l%2!=0:
    print("The new string is:",s[0]+s[l//2]+s[l-1])
else:
    print("The new string is:",s[0]+s[(l-1)//2]+s[(l//2)]+s[l-1])


