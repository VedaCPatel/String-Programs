#Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char
#of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on.
#Any leftover chars go at the end of the result.

s1=input("Enter string 1: ")
s22=input("Enter string 2: ")
s2=''
for i in s22[::-1]:
    s2+=i
s3=""
c1=0
c2=0
while c1!=len(s1) and


