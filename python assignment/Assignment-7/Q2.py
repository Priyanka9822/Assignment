#sum of all divisor of number
def sumDivisor(n):
    sum=0
    i=1
    while i<=n:
        if(n%i==0):
            print(i,end=" ")
            sum=sum+i
            i+=1
        else:
            i+=1
    return sum
num=int(input("Enter a number to calculate sum of all divisor:"))
r=sumDivisor(num)
print("sum of all divisor is=",r)