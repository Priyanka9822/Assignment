#Number of Vowels in string
s=input("Enter A String:")
count=0
for c in s:
    if c in"aeiouAEIOU":
        count+=1
print("Number of Vowels in String is:",count)