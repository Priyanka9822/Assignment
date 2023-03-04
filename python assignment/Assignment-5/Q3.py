def prime(n):
    sum=0
    for i in range(1,1+n):
        m=2
        while(m<=i-1):
            if(i%m==0):
                break
            else:
                m+=1
        if m==i:
            sum=sum+i
    print(" sum of all Prime no is=",sum)
pn=int(input("Enter a number to find a sum of prime no:"))
prime(pn)