#Remove Odd no Character in string
s=input("Enter A String:\t")
new=""
for c in range(len(s)):
    if c%2==0:
        new+=s[c]
print("OutPUT Of String:\t",new)