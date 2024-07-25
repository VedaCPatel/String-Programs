#Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced
#if all the characters in the s1 are present in s2. The character’s position doesn’t matter.
s1=input("Enter a string 1: ")#shorter
s2=input("Enter a string 2: ")
c=0
for i in s1:
    if i in s2:
        continue
    else:
        c+=1
if c==0:
    print("Balanced")
else:
    print("Unbalanced")