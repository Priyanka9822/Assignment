#print three digit reverse no#
num=145
for i in range(1,4):
    rev=num%10
    num=num//10
    print(rev,end="")
