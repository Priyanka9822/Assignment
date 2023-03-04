import math
def perfectsq(n):
    n1=math.sqrt(n)
    print(n1)
    n1=n1**2
    print(n1)
    if n1==n:
        print(n,"is perfect square")
    else:
        print(n,"is Not perfect square")
num=int(input("Enter a no to check perfect square or not="))
perfectsq(num)

