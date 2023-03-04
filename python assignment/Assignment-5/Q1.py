def factorial(n):
    sum=0
    for i in range(1,n+1):
        fact=1
        k=1
        while k<=i:
            fact=fact*k
            k+=1
        sum=sum+fact
    
    print(sum)
n=int(input("Enter a number to find sum of factorial series=\t"))
factorial(n)
#WITH argument WITH return#
def factorial(n):
    sum=0
    for m in range(1,n+1):
        fact=1
        i=1
        while i<=m:
            fact=fact*i
            i+=1
        sum=sum+fact
    return sum

num=int(input("Enter a number to find sum of factorial series=\t"))
r=factorial(num)
print("sum of factorial is=",r)