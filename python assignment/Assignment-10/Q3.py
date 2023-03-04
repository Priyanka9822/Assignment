#second largest element in list
max=0
smax=0
val=[45,78,94,12,34,56,54,102,78,25,30]
n=len(val)
for e in range(n):
    if max<val[e]:
        smax=max
        max=val[e]
    elif smax<val[e]:
        smax=val[e]

print("Second largest element in List is=",smax)