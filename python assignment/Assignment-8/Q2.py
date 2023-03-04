n=int (input("Enter the Number:"))
sum=0
for k in range(1,n+1):
    fact=1
    for l in range(1,k+1):
        fact=fact*l
    print("factorial is=",fact)
    sum=sum+(k/fact)
print("sum =",sum)
