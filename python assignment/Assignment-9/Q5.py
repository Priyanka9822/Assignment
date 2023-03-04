l=["digambar","swapnil","sagar","pka","priya","w"]
count=[]
for e in l:
    c=0
    for i in e:
        c+=1
    count.append(c)
print(count)
n=len(count)
for ele in range(1,n):
    for i in  range(n-ele):
        if(count[i]>count[i+1]):
            count[i],count[i+1]=count[i+1],count[i]
            l[i],l[i+1]=l[i+1],l[i]
    print(l)
print(l)    
l=["digambar","swapnil","sagar","pka","priya",1234]
count=[]
for e in l:
    q=str(e)
    c=0
    for i in (q):
        c+=1
    count.append(c)
print(count)
n=len(count)
for ele in range(1,n):
    for i in  range(n-ele):
        if(count[i]>count[i+1]):
            count[i],count[i+1]=count[i+1],count[i]
            l[i],l[i+1]=l[i+1],l[i]
    print(l)
print(l)    