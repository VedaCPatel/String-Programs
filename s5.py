#Given two strings, s1 and s2.
#Write a program to create a new string s3 by appending s2 in the middle of s1.

s1=input("Enter a string 1: ")
s2=input("Enter a string 2: ")
n1=""
n2=""
for i in s1[0:len(s1)//2]:
    n1+=i
for i in s1[(len(s1)//2):len(s1)]:
    n2+=i
print("The new string is :",n1+s2+n2)


