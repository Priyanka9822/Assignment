k=0
for i in range(1,10):
    if i<=5:
        k+=1
    else:
        k-=1
    for j in range(1,k+1):
        print("*",end=" ")
    print()
