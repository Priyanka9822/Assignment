# caculate no word and no chracter in string
s=input("Enter A string:")
space=" "
wc=1
cc=0
for c in s:
    if c==space:
        wc+=1
    else:
        cc+=1
print("Word in string are:",wc)
print("Character in strings Are:",cc)