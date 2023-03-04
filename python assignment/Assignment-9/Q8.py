#snake ladder
for i in range(10,0,-1):
    l=[]
    k=10
    for d in range(0,10):
        l.append(k*i-d)
    if i%2!=0:
        l.reverse()
        for m in l:
            print(m,end=" ")
    else:
        for m in l:
            print(m,end=" ")

    print()
print