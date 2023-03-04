def fact(m):
    if m==0:
        return 1
    else:

        return m *fact(m-1)
    
def sum(n):
    if n==0:
        return 0
    else:
         s=fact(n)+sum(n-1)
         return s
        
num=int(input("Enter a num="))
r=sum(num)
print(r,"is sum of upto ",num,"!",end=" ")
