#take two string Display Larger string

str1=input("Enter A Frist string:\t")
str2=input("Enter A Second string:\t")
c1=0
c2=0
for i in str1:
    c1+=1
for k in str2:
    c2+=1
if c1>c2:
    print("Larger String :\t",str1)
elif c1==c2:
    print("Both String Same Length")
else:
    print("Larger String :\t",str2)