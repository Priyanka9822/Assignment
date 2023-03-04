
for i  in range (1,6):
    k=i
    for j in range (1,7-i):
        if(i==2 and j==2 or i==2 and j==3 or i==3 and j==2):
            print(" ",end=" ")
            k+=1
        else:
            print(k,end=" ")
            k+=1 
    print()
print()
