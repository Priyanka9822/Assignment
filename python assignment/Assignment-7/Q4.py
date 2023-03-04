def perfectRange(a,b):
    for i in range(a,b+1):
        sum=0
        j=1
        while(j<=i-1):
            if i%j==0:
                sum=sum+j
                j+=1
            else:
                j+=1
        if sum==i:
            print(i,end=" ")
    else:print("Not found any perfect no")
sn=int(input("Enter a staring ange number:"))
en=int(input("Enter a ending range number:"))
perfectRange(sn,en)