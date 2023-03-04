data=[]
n=int(input("Eeter How many element enter="))
I=0
while(I<n):
    ele=int(input("Enter next value="))
    data.append(ele)
    I+=1
print(data)
n=len(data)
for i in range(1,n):
    for e in range(n-i):
        if(data[e]>data[e+1]):
            data[e],data[e+1]=data[e+1],data[e]
print(data)
slele=data[n-2]
print("Second Largest no is=",slele)