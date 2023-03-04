def rev(n,r):
    if n==0:
        return r

    else:
        m=rev(n//10,r*10+n%10)
        return m
num=int ( input("Enter a number"))
result=rev(num,0)
print(result)
