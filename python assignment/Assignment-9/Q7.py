# intersection
l1=[15,9,10,56,23,78,5,4,9,5]
l2=[9,4,5,36,47,26,10,45,87,5]
sl1=len(l1)
sl2=len(l2)
cl=[]
for el1 in range(sl1):
    for el2 in range(sl2):
        print(el2)
        if l1[el1]==l2[el2]:
                cl.append(l1[el1])
                break
print(cl)
