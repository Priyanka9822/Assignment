def arm(n,cube):
    
    if n==0:
        return 0
    else:
        N=n%10
        return N**3+arm(n//10,cube)    #N**3
        
num=int(input("Enter a number to check armstrong or not="))
r=arm(num,0)
if r==num:
    print(num,"is armstrong number")
else:
    print(num,"is Not armstrong number")