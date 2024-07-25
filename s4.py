#Given a string s, find the length of the longest substring without repeating characters.
s=input("Enter a string:")
n=''
c=0
for i in s:
    if i in n:
        continue
    else:
        n+=i
        c+=1
print("Length:",c)
print("The longest substring without repeating characters is:",n)