#create new list from existind list contain cube of each no
l=[1,2,3,4,5,6,7,8,9,10]
nl=[]
n=len(l)
for i in range(n):
    nl.append(l[i]**3)
print(nl)
