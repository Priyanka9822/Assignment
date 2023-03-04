'''def checkfibo(n):
    a=1
    b=0
    while(n>0):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
        if(c==n):
            print("yes")
            break
        else:
            if(c>n):
                print("not")
                break
num=int(input(" Enter no to check in fabanicc series or not"))
checkfibo(num)'''
def checkfibo(n):
    import math
    r=5*n*n+4
    print(r)
    s=5*n*n-4 
    print(s)
    
    p=math.sqrt(r)
    print(p)
    p=p**2

    print(p,end=" ")
    q=math.sqrt(s)
    print(q)
    q=q**2
    print(q,end=" ")
    if(r==p or q==s):
        print("yes")
    else:
        print("Not")
num=int(input(" Enter no to check in fabanicc series or not"))
checkfibo(num)