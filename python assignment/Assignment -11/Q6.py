#every blanck space replace as hyphen
s=input("Enter A String:")
space=" "
new=""
for c in s:
    if c==space:
        new+="-"
    else:
        new+=c
print("Output:",new,end=" ")