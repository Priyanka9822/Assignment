n=int(input("Enter the number to check Amstronge or not="))
temp=n
T=n
i=0
while n>0:
    N1=n%10
    n=n//10
    i+=1
print(i)
sum=0
if i==1:
    
    while temp>0:
        N1=temp%10
        print(N1)
        mul=N1
        sum=sum+mul
        temp=temp//10
if i==2:
    
    while temp>0:
        N1=temp%10
        print(N1)
        mul=N1*N1
        sum=sum+mul
        temp=temp//10
if i==3:
    
    while temp>0:
        N1=temp%10
        print(N1)
        mul=N1*N1*N1
        sum=sum+mul
        temp=temp//10
if i==4:
    
    while temp>0:
        N1=temp%10
        print(N1)
        mul=N1*N1*N1*N1
        sum=sum+mul
        temp=temp//10
if i==5:
    while temp>0:
        N1=temp%10
        print(N1)
        mul=N1*N1*N1*N1*N1
        sum=sum+mul
        temp=temp//10
print("SUM =",sum)
if sum==T:
            print(T,"is AMSTRONGE NUMBER")
else:
            print(T,"is NOT AMSTRONGE NUMBER")