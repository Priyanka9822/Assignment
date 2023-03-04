#check no is present in list or not how many times
l=[1,3,4,6,8,7,1,5,44,5,8,30]
n=len(l)
c=0
x=int(input("ENTER ANY NO:"))
for i in l:
    print(i)
    print(x)
    if(i==x):
        c=c+1
if(c>0):
    print(x,"is present in list,count is",c)
else:
    print(x,"is not present in list")