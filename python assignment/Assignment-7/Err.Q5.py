
def checkfibo(n):
    import math
    r=5*n*n+4
    print(r)
    s=5*n*n-4 
    print(s)

    p=(math.sqrt(r))
    p=p**2
    q=(math.sqrt(s))
    q=q**2
    if(r==p or q==s):
        print("yes")
    else:
        print("Not")
num=int(input(" Enter no to check in fabanicc series or not"))
checkfibo(num)