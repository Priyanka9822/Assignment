#to put even and odd element of a list into two different list


l=[]
n=int(input("Emter the how many no element enter="))
for i in range(n):
    ele=input("Enter the Next Element:")
    l.append(ele)
print(l)
even=[]
odd=[]
for e in l:
    if int(e)%2==0:
        even.append(e)      #even+=e
    else:
        odd.append(e)      #odd+=e
print("Even number List:",even)
print("odd number List:",odd)
