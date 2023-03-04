#TWO STRING ANAGRAM OR NOT
'''S1="LISTEN"
S2="SILENT"'''
S1=input("Enter A string:\t")
S2=input("Enter A string:\t")
c=0
s=len(S1)
for i in S1:
    for j in S2:
        if i.lower()==j.lower():
            c+=1
if s==c:
    print('String is Anagram')
else:
    print("String Is NOT Anagram")