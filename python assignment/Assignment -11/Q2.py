s=input("Enter A string:\t")
n=int(input('Enter A Index to remove Character:\t'))
ns=""
for i in range(len(s)):
    if i!=n:
        ns+=s[i]
print("String is=",ns)