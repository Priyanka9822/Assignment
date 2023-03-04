#given no perfect or not
def perfect(n):
    sum=0
    i=1
    while i<=n-1:
        if n%i==0:
            sum=sum+i
            i+=1
        else:
            i+=1
    if sum==n:
        print(sum,"is a perfect no")
    else:
         print(n,"Not a perfect no")
num=int(input("Enter a number to check perfect or not:"))
perfect(num)
