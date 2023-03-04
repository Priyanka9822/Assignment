for i in range(1,5):
    m=1
    for j in range(1,6-i):
        print(" ",end=" ")
    for k in range(1,(2*i+1)-1):
        if k<i:
            print(m,end=" ")
            m+=1
        else:
            print(m,end=" ")
            m-=1
    for l in range(1,6-i):
        print(" ",end=" ")
    print()