k=0

for m in range(1,10):
    if m<=5:
        k+=1
    else:
        k-=1
    for n in range(1,10):
        if (n>=6-k and n<=4+k):
            if m%2==0:
                if(n%2==0):
                    if (m==4 and n==4 or m==4 and n==6 or m==6 and n==4 or m==6 and n==6):
                        print(" ",end=" ")
                    else:
                        print("*",end=" ")
                else:
                    print(" ",end=" ")
            else:
                if n%2!=0:
                    if (m==3 and n==5 or m==5 and n==3 or m==5 and n==5 or m==5 and n==7 or m==7 and n==5):
                        print(" ",end=" ")
                    else:
                        print("*",end=" ")
                else:
                    print(" ",end=" ")
        else:
            print(" ",end=" ")
    print()
