
for i in range(1,6):
    k=1
    for j in range(1,10):
        if(j>=6-i and j<=4+i):
            if i%2!=0:
                if j%2!=0:
                    if j==5 and i==3:
                        print(" ",end=" ")
                        k+=1
                    else:
                        print(k,end=" ")
                        k+=1
                else:
                    print(" ",end=" ")
            else:
                if j%2==0:
                    if i==4 and j==4 or j==6 and i==4:
                        print(" ",end=" ")
                        k+=1
                    else:
                        print(k,end=" ")
                        k+=1
                else:
                    print(" ",end=" ")
                
        else:
            print(" ",end=" ")
    print()
print()

for i in range (1,6):
    for j in range(1,6-i):
         print(" ",end=" ")
        
    for j in range (1,i+1):
            if(i==5  or j==i or j==1):
                print(j,end="   ")
            else:
                print("  ",end="  ")
    print()
