# generate dictionar contain 1 to n no in form (n:n*n)
squ={}
n =int(input("Enter A Number:\t"))
for i in range(1,n+1):
    squ[i]=i*i 
print(squ)