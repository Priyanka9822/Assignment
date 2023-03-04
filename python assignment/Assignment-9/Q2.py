
l1=[]
e=int(input("How many element enter in list one="))
for i in range(e):
    ele=input("Enter next element")
    l1.append(ele)
l2=[]
e=int(input("How many element enter in list two="))
for i in range(e):
    ele=input("Enter next element")
    l2.append(ele)
l=[]
l.extend(l1)
l.extend(l2)
print(l1)
print(l2)
print(l)
n=len(l)
for e in range(1,n):
    for x in range(n-e):
        if l[x]>l[x+1]:
            l[x],l[x+1]=l[x+1],l[x]
print(l)
