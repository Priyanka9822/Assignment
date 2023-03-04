#WRITE  PG PRINT N PRIME NO
x=int(input("Enter a prime no"))
count=0
n=2
print('PRIME NO:',end=" ")
while count<x:
    m=2
    while(m<n): # THIS CONDITION IS WRITE IN ABOVE PROGEAM [M<=N-1THIS] ALSO WRITE
        if n%m==0:
            break
        else:
            m+=1
    if m==n:
        print(n,end=" ")
        n+=1
        count+=1
    else:
        n+=1

