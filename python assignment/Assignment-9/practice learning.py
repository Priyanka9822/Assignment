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
l=l1+l2
print(l1)
print(l2)
print(l)
print(id(l1))
print(id(l2))
print(id(l))
n=len(l)
for e in range(1,n):
    for x in range(n-e):
        if l[x]>l[x+1]:
            l[x],l[x+1]=l[x+1],l[x]
print(l)
'''l1=[]
e=int(input("How many element enter in list one="))
for i in range(e):
    ele=input("Enter next element")
    l1.append(ele)
l2=[]
e=int(input("How many element enter in list two="))
for i in range(e):
    ele=input("Enter next element")
    l2+=ele
l=l1+l2
print(l1)
print(l2)
print(l)
n=len(l)
for e in range(1,n):
    for i in range(n-e):
        if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
print(l)'''
l1=[12,18,25,35,25,20]
l2=[20,22,35,36,38,40]
nl1=set(l1)
nl2=set(l2)
l=[]
l.extend(nl1)
l.extend(nl2)
print(l)
n=len(l)
print(id(l))
'''for e in range(n):
    for p in range(e+1,n):
        if(l[e]!=l[p]):
            continue
        else:
            nl.append(l[e])
    else:
        ol.append(l[e])'''       
print(id(l1))
print(id(l2))