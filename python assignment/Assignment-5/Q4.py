def fabona(n,a,b):
    print(a,b,end=" ")
    while(n>2):
        c=a+b    
        a=b
        b=c
        n-=1
        print(c,end=" ")
    

t=int(input("Enter a no:"))
fabona(t,0,1)

'''def fabona(n):
    a=0
    b=1
    print(a,b,end=" ")
    i=3
    while(i<=n):
        c=a+b    
        a=b
        b=c
        i+=1
        print(c,end=" ")
t=int(input("Enter a no:"))
fabona(t)'''
