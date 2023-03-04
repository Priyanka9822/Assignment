for i in range(1,6):
    for j in range(1,10):
        if(j>=6-i and j<=4+i):
            if j<5:
                print(i,end=" ")
                i+=1
            else:
                print(i,end=" ")
                i-=1

        else:
            print(" ",end=" ")
    print()