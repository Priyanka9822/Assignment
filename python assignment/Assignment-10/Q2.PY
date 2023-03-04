#FIND THE MAXIMUN AND MINIMUM ELEMENT IN LIST
L=[45,90,75,100,79,80,25]
n=len(L)
for i in range(1,n):
    for x in range(n-i):
        if L[x]>L[x+1]:
            L[x],L[x+1]=L[x+1],L[x]
print("mimimum=",L[0])
print("maximun=",L[n-1])
#without using sort method
max=0
min=L[0]
for m in range(n):
    if max<L[m]:
        max=L[m]
    if min>L[m]:
        min=L[m]
print("min element is List=",min)
print("max element in List",max)