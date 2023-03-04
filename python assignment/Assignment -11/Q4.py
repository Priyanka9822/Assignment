s=input("Enter A string:")
f=s[0]
l=s[len(s)-1]
new=""
for i in range(len(s)):
    if i==0:
        new=new+l
    elif i==(len(s)-1):
        new=new+f 
    else:
        new+=s[i] 
print("Input:",s)
print("Output:",new)