def odd(n):
    sum=0
    for i in range(1,n+1):
        if(i%2!=0):
            sum=sum+i
    print("sum of Odd number is=",sum)
num=int(input("Enter the Number to find sun of odd Number:\t"))
odd(num)