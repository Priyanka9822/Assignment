n=int(input("print n prime no:"))
count=0
x=2
print(n,"prime no=",end=" ")
while count<n:             #count start from 0 then while condition < REQUIRED
    print(count)
    print(x)
    for i in range(2,x):
        if(x%i==0):
            x+=1
            break
    else:
        print("prime No:",x,end=" ")
        count+=1
        x+=1
#count start from 1 then while condition <= REQUIRED
n=int(input("print n prime no:"))
count=1
x=2
print(n,"prime no=",end=" ")
while count<=n:
    print(count)
    print(x)
    for i in range(2,x):
        if(x%i==0):
            x+=1
            break
    else:
        print(x,end=" ")
        count+=1
        x+=1
#WRITE  PG PRINT N PRIME NO
'''x=int(input("Enter a prime no"))
count=1
n=2
while count<=x:
    m=2
    for m in range(n-1,n+1):
        if n%m==0:
            break
        else:
            m+=1
    if m==n:
        print(n,end=" ")
        count+=1
    n+=1'''

        
'''x=int(input("Enter a prime no"))
count=0
n=2
while count<=x:
    m=2
    while(m<n-1):  #THIS CONDITION IS WRONGE N INCREMENT BUT THIS NOT PRINT PRIME
                    NO 4<4 F THEN M==N THIS COINDITION NEVER TRUE AFTER 2 PRINT
                    AND COUNTER NEVER INCRESE AFTER 1 AND N INCREMENT UPTO INFINITYBUT NOT PRINT
        if n%m==0:
            break
        else:
            m+=1
    if m==n:
        print(n)
        n+=1
        print(n)
        count+=1
        print(count)
    else:
        n+=1'''
x=int(input("Enter a prime no"))
count=0
n=2
while count<x:
    m=2
    while(m<n): # THIS CONDITION IS WRITE IN ABOVE PROGEAM [M<=N-1THIS] ALSO WRITE
        if n%m==0:
            break
        else:
            m+=1
    if m==n:
        print(n)
        n+=1
        print(n)
        count+=1
        print(count)
    else:
        n+=1