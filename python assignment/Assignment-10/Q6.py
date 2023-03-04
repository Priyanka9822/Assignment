#remove duplicate from list
l=[5,4,3,2,1,10,2,3,4,5]
for i in l:
    x=len(l)
    c=0
    for x in range(x):
        if(i==l[x]):
            c+=1
        if c>1:
            del l[x]
    print(l)