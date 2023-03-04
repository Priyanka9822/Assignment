def divisor(n):
    i=1
    while i<=n:
        if n%i==0:
            print(i,end=" ")
            i+=1
        else:
            i+=1
num=int(input("Enter a number to print all divisor=\t"))
divisor(num)
 